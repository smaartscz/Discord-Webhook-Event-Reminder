def add_new_event():
    from custom_functions.config import save_config
    add_another = True
    while add_another:
        new_artist = {}

        name = input("Event name: ")
        time = input("Event time: ")
        tag_role = input("Discord role? ")
        img = input("Link to image: ")

        new_artist = {"time": time, "role_id": tag_role, "img_url": img}

        #Loop though dictionary and save it
        for parameter in new_artist.items():
           key = parameter[0]
           value = parameter[1]
           save_config(name, key, value)

        #Ask user if he wants to add another event
        s = input("Add another event? Y/[N] ")
        s.lower()
        if s == "Y":
            add_another = True
        else:
            add_another = False

def modify():
    from custom_functions.config import modify_config, load_config, get_section, get_key, get_value
    from custom_functions.basic import clear
    import os
    
    clear()
    #Load configuration
    config = load_config()

    action = input('''
How do you want to modify config?
1) Add new event - add new
2) Remove event - remove
3) Change value of any key - modify
[4] Nothing
''')
    if action == "1" or action == "add new":
        add_new_event()

    elif action == "2" or action == "remove" or action == "delete":
        print("Available sections: "+ get_section())

        section = input("Enter full name of section: ")
        
        modify_config("2",section)

    elif action == "3" or action == "modify" or action == "change":
        print("Available sections: " + get_section())
        section = input("Enter full name of section: ")

        key = input("Enter full name of key that you want to change: " + get_key(section))

        print(f"Key {key} has value of " + get_value(section, key))
        value = input("Change to: ")

        modify_config("3", section, key, value)
