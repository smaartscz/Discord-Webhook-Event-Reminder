from configparser import ConfigParser
from custom_functions.f_time import get_time
from custom_functions.ui import add_new_event
config = ConfigParser()


#Create config
def create_config():
    config.read("config.cfg")

    webhook_url = input("Webhook URL: ")
    scheduled_time = input("Time when webhook should be sent(HH:MM): ")
    webserver = input("Do you want to allow HTTP Web server(True/[False]): ") or "False"

    if webserver == "True":
        webserver_port = input("What port should Web server run(Default: 80): ") or "80"
        webserver_path = input("Which folder should Web server use?(Default: custom_functions/web/web): ") or "custom_functions/web/web"

    #Add basic information
    config.add_section("General")
    config.set("General", "created", get_time())
    config.set("General", "modified", get_time())
    
    config.set("General", "name", "General")

    config.set("General", "webhook", webhook_url)

    config.set("General", "scheduled_time", scheduled_time)

    config.set("General", "allow_webserver", webserver)
    print(webserver)
    if webserver != "False":
        config.set("General", "webserver_port", webserver_port)
        config.set("General", "web_path", webserver_path)

    #Save config
    with open("config.cfg", "w") as f:
        config.write(f)

    #Generate empty index.html file for webserver
    if webserver != "False":
        web_path = webserver_path + "/index.html"
        with open(web_path, "w") as html:
            html.write("")
            html.close()

    print("Config successfully generated!")
    add_new_event()

def load_config():
    config.read("config.cfg")
    content = {}
    for section in config.sections():
        content[section] = dict(config.items(section))
    print("Config loaded successfully!")
    return content

def save_config(section, key, value):
    print("Saving config!")
    config.read("config.cfg")
    section_name = section.replace(" ","_")
    try:
        config.set(section_name, "modified", get_time())
        config.set(section_name, key, value)
        with open("config.cfg", "w") as f:
          config.write(f)
    except:
        config.add_section(section_name)
        config.set(section_name, "created", get_time())
        config.set(section_name, "modified", get_time())
        config.set(section_name, "has_finished", "False")
        config.set(section_name, "name", section)
        config.set(section_name, key, value)
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