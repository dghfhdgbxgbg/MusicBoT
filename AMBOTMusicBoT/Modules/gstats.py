import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from AMBOTMusicBoT import app
from AMBOTMusicBoT.database.db import get_served_chats, get_served_users
from config import PING_IMG


@app.on_message(filters.command(["gstats"]) & filters.group)
async def gstats(client, message: Message):
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    await message.reply_photo(
        photo=PING_IMG,
        caption= f"served chats = {served_chats}\nserved users = {served_users}"
    )
