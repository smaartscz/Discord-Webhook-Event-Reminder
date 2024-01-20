import os
import schedule
import time
from functions import create_config, check_events, load_config
print("PoC")

# Check if config already exists or it's first time running this app
if not os.path.isfile("config.cfg"):
     create_config()

def main():
     check_events()
     print(check_events())

#Load config and set up schedule
config = load_config()
scheduled_time = config["main"]["scheduled_time"]
print(scheduled_time)
schedule.every().day.at(scheduled_time).do(main)


while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep to avoid high CPU usage