from custom_functions.config import create_config, load_config
from custom_functions.webhook import prepare_webhook
import os
import schedule
import time


print("PoC")

# Check if config already exists or it's first time running this app
if not os.path.isfile("config.cfg"):
     create_config()

#Load config and set up schedule
config = load_config()
scheduled_time = config["main"]["scheduled_time"]
schedule.every().day.at(scheduled_time).do(prepare_webhook)


while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep to avoid high CPU usage