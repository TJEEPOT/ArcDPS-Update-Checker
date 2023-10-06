# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Sends the latest update found by update_check.py to Discord.
Project : ArcDPS-Update-Checker
File    : output.py
Date    : Thursday 05 October 2023
History : 2023/10/05 - v0.1 - Create project file
"""

""" Copyright Martin Siddons - All Rights Reserved
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential
    Written by Martin Siddons <tjeepot@gmail.com>, October 2023
"""

__author__     = "Martin Siddons"
__email__      = "tjeepot@gmail.com"
__status__     = "Development"  # "Development" "Prototype" "Production"

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv

def to_discord(update_message):
    load_dotenv() # load the .env file
    discord_webhook = os.getenv("discord_webhook")

    if discord_webhook is None:
        print("ERROR: Discord Webhook not found. Have you included it as an environment variable?", file=sys.stderr)
        return
    
    notify_discord(discord_webhook, update_message)


def notify_discord(webhook, message):
    content = f"ArcDPS has been updated!"

    author = {
        "name": "ArcDPS Update Checker",
        "url": "https://github.com/TJEEPOT/ArcDPS-Update-Checker/",
    }
    
    url = "https://www.deltaconnected.com/arcdps/"
    
    webhook = DiscordWebhook(url=webhook, content=content)
    embed = DiscordEmbed(author=author, color="3e68cb", title=message, url=url)
    webhook.add_embed(embed)
    response = webhook.execute()

    if response.status_code != 200:
        print(f"Unusual response from Discord: {response.text}")
    else:
        print("Message sent to Discord.")
    

if __name__ == "__main__":
    print("Incorrect file run. Please run update_check.py instead.")