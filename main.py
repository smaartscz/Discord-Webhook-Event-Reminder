from custom_functions.config import create_config, load_config
from custom_functions.webhook import prepare_webhook
from custom_functions.ui import add_new_event
import os, schedule, time, sys


print("PoC")
if len(sys.argv) > 1:
     arg = sys.argv[1]
     if arg == "add" or arg == "--add":
          print(arg)
          add_new_event()
     else:
          print(f"Unknown argument! Got {arg}")

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