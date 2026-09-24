import os
import time
import importlib
import asyncio

from pyrogram import Client
from pytgcalls import PyTgCalls

from Codexun import config


SUDO_USERS = config.SUDO_USERS
OWNER_ID = config.OWNER_ID
BOT_ID = config.BOT_ID

BOT_NAME = ""
BOT_USERNAME = ""

ASSID = config.ASSID
ASSNAME = ""
ASSUSERNAME = ""

SUDOERS = SUDO_USERS
OWNER = OWNER_ID

# Boot Time
boottime = time.time()

# =========================================================
# Assistant STRING SESSION
# =========================================================

STRING_SESSION = os.getenv("STRING_SESSION")

if not STRING_SESSION:
    raise RuntimeError(
        "STRING_SESSION is missing. "
        "Please add STRING_SESSION to Deployzy Environment Variables."
    )

# Assistant account
smexy = Client(
    "assistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=STRING_SESSION,
)

# PyTgCalls uses the same Assistant client
pytgcalls = PyTgCalls(smexy)

# Music Start Time
Music_START_TIME = time.time()

# =========================================================
# Bot client
# =========================================================

app = Client(
    "codexunmusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

# =========================================================
# Information
# =========================================================

def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSUSERNAME

    getme = app.get_me()
    getme1 = client.get_me()

    BOT_ID = getme.id
    ASSID = getme1.id

    if getme.last_name:
        BOT_NAME = f"{getme.first_name} {getme.last_name}"
    else:
        BOT_NAME = getme.first_name

    BOT_USERNAME = getme.username

    if getme1.last_name:
        ASSNAME = f"{getme1.first_name} {getme1.last_name}"
    else:
        ASSNAME = getme1.first_name

    ASSUSERNAME = getme1.username


# =========================================================
# Start
# =========================================================

app.start()
smexy.start()

all_info(app, smexy)

# Keep old variable name compatible with the rest of the project
client = smexy
