# What It Does #
Small script to check if there has been an update to ArcDPS since it last checked and if so, send a discord webhook message to a given channel.

# Usage Notes #
In order to work correctly, you will also need to provide your Discord webhook as an environment variable. To add an environment variable, create a file in the project folder named ```.env``` and type ```#.env``` on the first line, and ```discord_webhook=``` followed by the URL of your Discord webhook on the second (no quotes needed).

This script is written in Python 3, therefore I recommend installing the latest version of
 [Python](https://www.python.org/downloads/) to run it. Once installed, do the following:
 - Open a Terminal / Command Line / Powershell prompt in the folder the script is in and type ```python3 -m venv .venv``` to build a virtual environment for the scripts to run in. 
 - Activate the virtual environment with ```.\.venv\Scripts\activate.bat``` in Windows Command Line, ```.\.venv\Scripts\activate.ps1``` in Windows Powershell or ```source \.venv\Scripts\activate``` on Linux or Mac.
 - Load the required libraries with ```pip install -r requirements.txt```.
 - type ```python3 notifier.py``` to run the program.

I'd recommend setting up a task / cron to run ```update_check.py``` every day or two to ensure you don't miss out on an update.