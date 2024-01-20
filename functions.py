from discord_webhook import DiscordWebhook, DiscordEmbed
from configparser import ConfigParser
from datetime import datetime
from time import time
import os
config = ConfigParser()
add_another = True
#Create config

def create_config():
    config.read("config.cfg")
    webhook_url = input("Webhook URL: ")
    scheduled_time = input("Time(12:00): ")
    
    config.add_section("main")
    config.set("main", "created", str(datetime.now()))
    config.set("main", "modified", str(datetime.now()))
    config.set("main", "webhook", webhook_url)
    config.set("main", "scheduled_time", scheduled_time)

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

    #Create new section
    try:
        config.add_section(section)
        config.set(section, "created", str(datetime.now()))
        config.set(section, "modified", str(datetime.now()))
        config.set(section, "has_finished", "False")
        config.set(section, "name", section)
        config.set(section, key, value)
        with open("config.cfg", "w") as f:
            config.write(f)
    # If exists then save it
    except:
        save_config(section, key, value)

def save_config(section, key, value):
    config.read("config.cfg")
    config.set(section, "modified", str(datetime.now()))
    config.set(section, key, value)
    with open("config.cfg", "w") as f:
        config.write(f)

def remaining_time(unix_time):
    #Get remaining time
    current_time = int(time())

    #Convert it days
    days = str(int((int(unix_time) - current_time) / 86400)) + " dní "
    print(days)
    return days
    
def send_webhook(name, unix_time, days, embed_color, next):
    #Create new instance
    webhook = DiscordWebhook(url=f'{config["main"]["webhook"]}', content=f'<@&{config[name]["role_id"]}>')

    #Configure message
    embed = DiscordEmbed(title=f'{config[name]["name"]}', description=f'Akce začíná za: {days} (<t:{unix_time}:R>)', color=embed_color)
    embed.set_author(name=name, icon_url=config[name]["img_url"]) 
    embed.set_footer(f"Další akce je: {next}")
    #Add it to message
    webhook.add_embed(embed)

    #Send webhook
    response = webhook.execute()
    print(response)

#Load upcoming events
def load_events():
    #Load config
    config = load_config()

    #Create empty dictionary
    events = {}

    #Loop though config and check if there are upcoming events
    for event in config:
        if event != "main":
            if config[event]["has_finished"] == "False":
                events[event] = config[event]["time"]
    return events

def prepare_webhook():
    #Load events
    events = load_events()
    #Create empty directories for upcoming and next events
    upcoming = {}
    next = {}

    #Store upcoming and next event into directory
    for event in events:
        if upcoming == {}:
            upcoming["name"] = event
            upcoming["time"] = events[event]
        elif next == {}:
            next["name"] = event
            next["time"] = events[event]

    print(events)
    print(upcoming)
    print(next)

    #Get remaining time
    days = remaining_time(upcoming["time"])

    #Get color based if its today or no
    if days == 0:
        embed_color = "1BFF00"
    else:
        embed_color = "001BFF"
    send_webhook(upcoming["name"], upcoming["time"], days, embed_color, next["name"])




prepare_webhook()
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
    s = input("Pridat dalsi akci? Ano/Y/Ne/[N] ")
    if s == "Ano" or s == "Y" or s == "y":
        add_another = True
    else:
        add_another = False
'''