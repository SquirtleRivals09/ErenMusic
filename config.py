import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "24620300"
API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7825465869:AAEFYQ_rVGLQTcXHJkxktYCa0I5uQaXVuTY"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://dnmusic97:HAMENHIPATAPASSWORD%268191@testingdb.bgb0v.mongodb.net/?retryWrites=true&w=majority&appName=Testingdb"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1001836376079

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = 5458968679

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Smaugopp/Voidmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hunterXsupport")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hunterXsupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = "BQFvkJcAZv4J56F5uhyI_6kPKGw0wj09moO_md59Np1hrpbuDpzlZQd7ecupJAGdd0HrJBxdMvTcE3GhoqPBXbfD5WzmJgWyYujjyklcFH0GYq0TChaFLB7LM0xhU7ND8Vxv6M5eIBAtAcNEhxzaGCVRItRF8cmO7Pqlu5gSm4UOIC2r_oSDAHM85ltgxxJle3_MlfUlURik21rz1GUzQ-w6LO5B9bmTMrJHI1ocSb5yTAVJ3bLfzO9f3lVwQmnJ9YnG22aZqdWqiBxVNEf_cz4tPMjx89RXcMedkyyG76SrgZ6DF-QcjTTfiBj03cMWXnZ1D5rW3u-PCQ50L_7py7DBq9IyuAAAAAHVutsxAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/01ba8cd4c05f3f83af28c-f8afa1b0676f1fa92c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/4fdaf06331c40028651c9-d78d4bd2b7dfcae80e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/b62173af4bca080eb2556-4e535d45b195bba255.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
STREAM_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/97669c286e18c2eddc72d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
