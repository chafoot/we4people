import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "5555669937:AAGFc2aiVS378Y0vbccPGHC0b2cddcAroyI")
BOT_NAME = getenv("BOT_NAME", "Our People Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tgbotproject")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "27709822"))
API_HASH = getenv("API_HASH", "a30de8d316e15153c76c64342b86546b")
BOT_USERNAME = getenv("BOT_USERNAME", "we4peoplebot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "YTDOKI-QIDCUM-MFCHKC-TZMFHX-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001707561361")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
