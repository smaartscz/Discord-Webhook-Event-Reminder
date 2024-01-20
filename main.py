from custom_functions.config import create_config, load_config
from custom_functions.webhook import prepare_webhook
from custom_functions.ui import modify
import os, schedule, time, sys


print("PoC")
if len(sys.argv) > 1:
     print("Argument detected!")
     arg = sys.argv[1].lower()
     if arg == "modify":
          modify()
     else:
          print(f"Unknown argument! Got {arg}. Continuing as usual.")
os.system("cls")
# Check if config already exists or it's first time running this app
if not os.path.isfile("config.cfg"):
     print("Running for first time! Creating new config")
     create_config()


#Load config and set up schedule
print("Loading configuration!")
config = load_config()
scheduled_time = config["General"]["scheduled_time"]

print("Setting up schedule!")
schedule.every().day.at(scheduled_time).do(prepare_webhook)

print("Startup successful! Continuing as usual.")
while True:
     schedule.run_pending()
     time.sleep(1)  # Sleep to avoid high CPU usage