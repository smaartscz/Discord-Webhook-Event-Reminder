from configparser import ConfigParser
from custom_functions.f_time import get_time
from custom_functions.ui import add_new_event
config = ConfigParser()


#Create config
def create_config():
    config.read("config.cfg")
    webhook_url = input("Webhook URL: ")
    scheduled_time = input("V kolik hodin mám pingovat?(HH:MM): ")
    
    #Add basic information
    config.add_section("General")
    config.set("General", "created", get_time())
    config.set("General", "modified", get_time())
    config.set("General", "webhook", webhook_url)
    config.set("General", "scheduled_time", scheduled_time)

    with open("config.cfg", "w") as f:
        config.write(f)

    print("Config successfully generated!")
    add_new_event()

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
    # If section exists then save it
    except:
        save_config(section, key, value)

def save_config(section, key, value):
    print("Saving config!")
    config.read("config.cfg")
    try:
        config.set(section, "modified", get_time())
        config.set(section, key, value)
        with open("config.cfg", "w") as f:
          config.write(f)
    except:
        config.add_section(section)
        config.set(section, "created", get_time())
        config.set(section, "modified", get_time())
        config.set(section, "has_finished", "False")
        config.set(section, "name", section)
        config.set(section, key, value)
        with open("config.cfg", "w") as f:
            config.write(f)   
    print("Config saved!") 

def modify_config(action, section, key="", value=""):
    config.read("config.cfg")
    action = action.lower()
    #Delete section
    if action == "2":
        print(f"Removing section: {section}")
        config.remove_section(section)
    else:
        print(f"Modifing section: {section}, key: {key}, value: {value}")
        save_config(section, key, value)

    #Save file
    with open("config.cfg", "w") as f:
        config.write(f)
    print("Section removed!")

def get_section():
    sections = "\n"
    for section in config:
        if section != "DEFAULT":
            sections += section + "\n"
    return sections

def get_key(section):
    keys = "\n"
    for key in config[section]:
        keys += key + "\n"
    return keys
def get_value(section, key):
    value = config[section][key]
    return value