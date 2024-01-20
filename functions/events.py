from config import load_config

#Load upcoming events
def load_events():
    #Load config
    config = load_config()

    #Create empty dictionary
    events = []
    
    #Loop though config and check if there are upcoming events
    for event in config:
        new_event = {}
        if event != "main":
            if config[event]["has_finished"] == "False":
                new_event["id"] = event
                new_event["name"] = config[event]["name"]
                new_event["time"] = config[event]["time"]
                events.append(new_event)
    
    return events