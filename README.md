Barberhood Booking Monitor 💈

A lightweight Python script that monitors thebarberhood.co.uk
 every 10 minutes for new or cancelled booking slots within the next 14 days.
When a new slot is found, it sends you an instant Telegram notification.

⚠️ Note: I got permission from my barber to run this script. Please make sure to get permission from your barber before using it. Let’s keep the barbers happy and avoid any “hair-raising” situations! 😄

🚀 Features

Checks for new or cancelled bookings automatically.

Monitors slots up to 14 days in advance.

Sends real-time notifications via Telegram.

Lightweight and easy to run on your local machine.

⚡ Setup

Clone the repository:

git clone https://github.com/EliasH444/barberhood-booking-bot.git
cd barberhood-booking-bot


Install dependencies:

pip install -r requirements.txt


Configure your Telegram bot:

Create a Telegram bot via BotFather
.

Get your bot token and chat ID.

Add them to the config.json (or .env file if used) in the project.

Run the script:

python main.py


The script will now check for available slots every 10 minutes and send notifications to your Telegram account.

🔧 How to Adapt the Script

Change the website: You can modify the URL in the script to monitor a different booking website.

Adjust the time frame: Update the script to check for slots beyond 14 days if needed.

Modify notification method: Instead of Telegram, you can integrate email, SMS, or push notifications.

Change check interval: Adjust the frequency (currently every 10 minutes) to suit your needs.

Filter specific barbers or services: Add logic to only notify you for certain barbers, locations, or services.

With a little Python knowledge, this script can become your personal booking assistant for almost any appointment-based website.

🛠️ Notes

Make sure your PC is connected to the internet while the script is running.

Designed to run locally, but can be adapted for a server or cloud deployment.

💡 Contributions

Feel free to fork this repository and suggest improvements or additional features!

Remember: always ask for permission before checking someone else’s bookings. We don’t want the barber giving you the “silent treatment” 😅
