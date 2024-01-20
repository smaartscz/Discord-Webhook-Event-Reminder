from datetime import datetime

import os
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
        add_new(name, key, value)

    #Ask user if he wants to add another artist
    s = input("Pridat dalsi akci? Ano/Y/Ne/[N] ")
    if s == "Ano" or s == "Y" or s == "y":
        add_another = True
    else:
        add_another = False
