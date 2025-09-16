import requests
import time
import datetime
from bs4 import BeautifulSoup
import telegram

# --- CONFIG ---
URL = "https://www.thebarberhood.co.uk/bookings"  # Booking page
CHECK_INTERVAL = 600  # 10 minutes in seconds
DAYS_AHEAD = 14  # Check for slots in the next 14 days

# Telegram bot details
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Track seen slots
seen_slots = set()

def fetch_slots():
    """Scrape available slots from booking website."""
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # This part depends on the site's HTML structure.
        # Adjust selectors if needed.
        slots = []
        for slot in soup.find_all("div", class_="booking-slot"):
            date_str = slot.get("data-date")
            time_str = slot.get("data-time")

            if date_str and time_str:
                slot_time = datetime.datetime.strptime(
                    f"{date_str} {time_str}", "%Y-%m-%d %H:%M"
                )
                if slot_time.date() <= (datetime.datetime.now().date() + datetime.timedelta(days=DAYS_AHEAD)):
                    slots.append(slot_time.strftime("%Y-%m-%d %H:%M"))

        return slots

    except Exception as e:
        print(f"[ERROR] Failed to fetch slots: {e}")
        return []

def notify_new_slots(new_slots):
    """Send Telegram notification for new slots."""
    message = "💈 New booking slot(s) available:\n" + "\n".join(new_slots)
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    global seen_slots
    print("🚀 Barber booking monitor started...")

    while True:
        slots = fetch_slots()

        new_slots = [s for s in slots if s not in seen_slots]
        if new_slots:
            print(f"[INFO] Found new slots: {new_slots}")
            notify_new_slots(new_slots)
            seen_slots.update(new_slots)
        else:
            print("[INFO] No new slots found.")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
