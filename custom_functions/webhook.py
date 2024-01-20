from discord_webhook import DiscordWebhook, DiscordEmbed
from custom_functions.config import load_config, save_config
from custom_functions.events import load_events
from custom_functions.f_time import remaining_time

def send_webhook(id, name, unix_time, time, embed_color, next):
    config = load_config()
    #Create new instance
    webhook = DiscordWebhook(url=f'{config["main"]["webhook"]}', content=f'<@&{config[id]["role_id"]}>', avatar_url=config[id]["img_url"], username=config[id]["name"])

    #Configure message
    embed = DiscordEmbed(title=f'Blíží se událost!', description=f'Akce začíná za: {time}(<t:{unix_time}:R>)', color=embed_color)
    embed.set_author(name=name, icon_url=config[id]["img_url"]) 
    embed.set_footer(f"{next}")
    #Add it to message
    webhook.add_embed(embed)

    #Send webhook
    response = webhook.execute()
    print(response)



def prepare_webhook():
    #Load events
    events = load_events()

    #Format events for easier use
    upcoming_id = events[0]["id"]
    upcoming_name = events[0]["name"]
    upcoming_time = events[0]["time"]

    try:
        next = "Další akce bude " + events[1]["name"]
    except:
        next = "Žádná další akce není :("

    #Get remaining time
    days, hours = remaining_time(events[0]["time"])

    #Get color based if its today or no
    if days == 0:
        embed_color = "1BFF00"
        time_text = f"{hours} hodin"

        #Save it as finished event
        save_config(section=upcoming_id, key="has_finished", value="True")
    else:
        embed_color = "001BFF"
        time_text = f"{days} dní a {hours} hodin"
    send_webhook(id=upcoming_id,name=upcoming_name, unix_time=upcoming_time, time=time_text, embed_color=embed_color, next=next)