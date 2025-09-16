# Barberhood Booking Monitor 💈

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Notifications-blue?logo=telegram&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/EliasH444/barberhood-booking-bot)

A lightweight Python script that monitors my local babers every 10 minutes for **new or cancelled booking slots** within the next 14 days.  
When a new slot is found, it sends you an instant **Telegram notification**.

> ⚠️ **Note:** I got permission from my barber to run this script. **Please make sure to get permission from your barber before using it.**  
> Let’s keep the barbers happy and avoid any “hair-raising” situations! 😄

---

## 🚀 Features
- Automatic monitoring for new or cancelled bookings.
- Checks slots up to 14 days in advance.
- Sends real-time Telegram notifications.
- Lightweight and easy to run locally.

---

## ⚡ Setup

1. **Clone the repository**:  
```bash
git clone https://github.com/EliasH444/barberhood-booking-bot.git
cd barberhood-booking-bot

2.**Install dependencies**:

pip install -r requirements.txt
Configure your Telegram bot:
Create a Telegram bot via BotFather
Get your bot token and chat ID.
Add them to the BookingBot.Py file in the project.
Run the script:
python main.py



🔧 How to Adapt the Script

Change the website: Modify the URL to monitor a different booking website.
Adjust the time frame: Check for slots beyond 14 days.
Modify notifications: Use email, SMS, or push notifications instead of Telegram.
Change check interval: Adjust the frequency (currently every 10 minutes).
Filter specific barbers or services: Only notify for selected barbers, locations, or services.
With a little Python knowledge, this script can become your personal booking assistant for almost any appointment-based website.

🛠️ Notes

Ensure your PC is connected to the internet while running the script.
Designed for local execution but can be adapted for cloud/server deployment.

💡 Contributions

Feel free to fork this repository and suggest improvements or additional features!
Remember: always ask for permission before checking someone else’s bookings. We don’t want the barber giving you the “silent treatment” 😅