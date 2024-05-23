
import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from config import OWNER_ID
from AMBOTMusicBoT import ASS_MENTION, SUNAME, app, app2


@app.on_message(filters.command(["leaveall", "assleaveall"]) & filters.user(OWNER_ID))
async def ass_leaveall(_, message: Message):
    lear = await message.reply_text(f"» {ASS_MENTION} 𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝘾𝙝𝙖𝙩...")
    left = 0
    failed = 0
    chats = []
    async for dialog in app2.get_dialogs():
        chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(SUNAME)).id
    for i in chats:
        if i in (-1001596737491, int(schat)):
            continue
        try:
            await app2.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
            failed += 1
    try:
        await lear.edit_text(
            f"<u>**» {ASS_MENTION} 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙡𝙚𝙛𝙩 𝘾𝙝𝙖𝙩 :**</u>\n\n**𝙡𝙚𝙛𝙩 :** `{left}`\n**𝙁𝙖𝙞𝙡𝙚𝙙 :** `{failed}`"
        )
    except:
        await message.reply_text(
            f"<u>**» {ASS_MENTION} 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙡𝙚𝙛𝙩 𝘾𝙝𝙖𝙩 :**</u>\n\n**𝙡𝙚𝙛𝙩 :** `{left}`\n**𝙁𝙖𝙞𝙡𝙚𝙙 :** `{failed}`"
        )
