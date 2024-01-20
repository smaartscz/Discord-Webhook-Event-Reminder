from discord_webhook import DiscordWebhook, DiscordEmbed
from configparser import ConfigParser
import os
from functions import create_config, load_config, add_new, save_config

# Check if config already exists or it's first time running this app
if not os.path.isfile("config.cfg"):
     create_config()

print(config["Architects"])

 #Load config
config = load_config()

#Create new instance
webhook = DiscordWebhook(url=f'{config["main"]["webhook"]}', content=f'<@&{config["Architects"]["role_id"]}>')

#Configure message
embed = DiscordEmbed(title=f'{config["Architects"]["name"]}', description=f'Akce začíná za: (<t:{config["Architects"]["time"]}:R>)', color="03b2f8")
embed.set_author(name="Architects", icon_url=config["Architects"]["img_url"]) 

#Add it to message
webhook.add_embed(embed)

# Send webhook
response = webhook.execute()
print(response)