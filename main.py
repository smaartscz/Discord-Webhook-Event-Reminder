from discord_webhook import DiscordWebhook
from configparser import ConfigParser
import os
from functions import create_config, load_config, add_new, save_config


if not os.path.isfile("config.cfg"):
     create_config()
config = load_config()
print(config["Architects"]["has_finished"])