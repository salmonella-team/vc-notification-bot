# setting.py

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID")
UEKI_CHANNEL_ID = os.environ.get("UEKI_CHANNEL_ID")