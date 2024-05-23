

import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from AMBOTMusicBoT import BOT_NAME, StartTime, app
from AMBOTMusicBoT.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} 𝙄𝙨 𝙋𝙞𝙣𝙜𝙞𝙣𝙜...."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""𝙋𝙤𝙣𝙜 : `{resp}𝙈𝙨`

<b><u>{BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨 :</u></b>

✾ **𝙐𝙥𝙩𝙞𝙢𝙚 :** {uptime}
✾ **𝙍𝙖𝙢 :** {mem}
✾ **𝘾𝙥𝙪 :** {cpu}
✾ **𝘿𝙞𝙨𝙠 :** {disk}
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT)
                ],
            ]
        ),
    )
