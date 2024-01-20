def add_new_event():
    from custom_functions.config import save_config
    add_another = True
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
           save_config(name, key, value)

        #Ask user if he wants to add another artist
        s = input("Pridat dalsi akci? Ano/Y/Ne/[N] ")
        if s == "Ano" or s == "Y" or s == "y":
            add_another = True
        else:
            add_another = False

def modify():
    from custom_functions.config import modify_config, load_config, get_section, get_key, get_value
    import os
    os.system("cls")
    #Load configuration
    config = load_config()

    action = input('''
Co chceš udělat?
1) Přidat novou akci - add new
2) Smazat akci - remove
3) Změnit hodnotu - modify
[4] Nic
''')
    if action == "1" or action == "add new":
        add_new_event()

    elif action == "2" or action == "remove" or action == "delete":
        print("Dostupné sekce: "+ get_section())

        section = input("Zadej celý název sekce: ")
        
        modify_config("2",section)

    elif action == "3" or action == "modify" or action == "change":
        print("Dostupné sekce: " + get_section())
        section = input("Zadej celý název sekce: ")

        key = input("Zadej celý název položky, kterou chceš změnit: " + get_key(section))

        print(f"Momentálně má {key} hodnotu " + get_value(section, key))
        value = input("Změnit na: ")

        modify_config("3", section, key, value)
