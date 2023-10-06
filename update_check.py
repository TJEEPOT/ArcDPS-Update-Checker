# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Script to get the latest update from deltaconnected.com/arcdps/ and check if that matches the last update. If it doesn't, it triggers an output to Discord and updates.
Project : ArcDPS-Update-Checker
File    : update_check.py
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

import output

import requests
import re

def get_current_page():
    s = requests.session()
    url = f"https://www.deltaconnected.com/arcdps/"
    headers = {"User-Agent": "ArcDPS-Update-Checker", #  good practice to remain contactable with web admins
                     "From": "https://github.com/TJEEPOT/ArcDPS-Update-Checker"}  
    response = s.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise AssertionError(f"Incorrect status code received ({response.status_code}).")
    else:
        return response.text

def find_last_update(page):
    text = re.findall(r"(?:<b>changes<\/b><br>)\s*(.*)", page)[0]
    text_remove_intro = text.removeprefix("&nbsp;")
    text_remove_ending = text_remove_intro.removesuffix("<br>")
    return text_remove_ending

def get_previous_update():
    with open("last_update.txt", "r") as f:
        last_update = f.readline()
    return last_update

def write_previous_update(update):
    with open("last_update.txt", "w") as f:
        f.write(update)
    print("Updated last_update.txt")

if __name__ == "__main__":
    page = get_current_page()
    latest_update = find_last_update(page)
    previous_update = get_previous_update() #  get the saved update from the last time the script updated it

    if latest_update == previous_update:
        print("There is no new update.")
        exit()

    write_previous_update(latest_update)
    output.to_discord(latest_update)

    