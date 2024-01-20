from configparser import ConfigParser
from custom_functions.f_time import get_time

config = ConfigParser()


#Create config

def create_config():
    config.read("config.cfg")
    webhook_url = input("Webhook URL: ")
    scheduled_time = input("Time(12:00): ")
    
    config.add_section("main")
    config.set("main", "created", get_time())
    config.set("main", "modified", get_time())
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
        config.set(section, "created", get_time())
        config.set(section, "modified", get_time())
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
    config.set(section, "modified", get_time())
    config.set(section, key, value)
    with open("config.cfg", "w") as f:
        config.write(f)