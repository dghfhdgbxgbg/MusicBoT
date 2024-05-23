
import asyncio
import importlib
import os

from pyrogram import idle

from AMBOTMusicBoT import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from AMBOTMusicBoT.Modules import ALL_MODULES


async def AMBOT_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("AMBOTMusicBoT.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"❇ ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ ❇\n\n⎋ ɪᴅ : `{BOT_ID}`\n⎋ ɴᴀᴍᴇ : {BOT_NAME}\n⎋ ᴜꜱᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"❇ ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ ᴀꜱꜱ ❇\n\n⎋ ɪᴅ : `{ASS_ID}`\n⎋ ɴᴀᴍᴇ : {ASS_NAME}\n⎋ ᴜꜱᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ Bot Started As {BOT_NAME}.")
    LOGGER.info(f"[•] ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ loaded "
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(AMBOT_startup())
    LOGGER.error("ᴀᴍʙᴏᴛ ᴍᴜꜱɪᴄ Bot Stopped.")
