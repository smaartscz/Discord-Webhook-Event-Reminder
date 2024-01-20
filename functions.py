from discord_webhook import DiscordWebhook
from configparser import ConfigParser
import datetime
import os
config = ConfigParser()
add_another = True
#Create config

def create_config():
    config.read("config.cfg")
    webhook_url = input("Webhook URL: ")
    
    config.add_section("main")
    config.set("main", "created", str(datetime.datetime.now()))
    config.set("main", "modified", str(datetime.datetime.now()))
    config.set("main", "webhook", webhook_url)
    with open("config.cfg", "w") as f:
        config.write(f)

def load_config():
    config.read("config.cfg")
    content = {}
    for section in config.sections():
        content[section] = dict(config.items(section))
    return content

def add_new(section, key, value):
    config.read("config.cfg")
    try:
        config.add_section(section)
        config.set(section, "created", str(datetime.datetime.now()))
        config.set(section, "modified", str(datetime.datetime.now()))
        config.set(section, "has_finished", "False")
        config.set(section, key, value)
        with open("config.cfg", "w") as f:
            config.write(f)
    except:
        save_config(section, key, value)

def save_config(section, key, value):
    config.read("config.cfg")
    config.set(section, "modified", str(datetime.datetime.now()))
    config.set(section, key, value)
    with open("config.cfg", "w") as f:
        config.write(f)
'''
while add_another:
    new_artist = {}

    name = input("Název akce: ")
    time = input("Čas akce: ")
    tag_role = input("Jakou roli mám tagnout? ")
    img = input("Odkaz na image: ")

    new_artist = {"time": time, "role_id": tag_role, "img_url": img}

    #Loop though dictionary and save it
    for parameter in new_artist.items():
        key = parameter[0]
        value = parameter[1]
        add_new(name, key, value)

    #Ask user if he wants to add another artist
    s = input("Pridat dalsi akci? Ano/Y/Ne/[N]")
    if s == "Ano" or s == "Y" or s == "y":
        add_another = True
    else:
        add_another = False
'''