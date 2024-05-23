

from pyrogram import filters
from pyrogram.types import Message

from AMBOTMusicBoT import SUDOERS, app
from AMBOTMusicBoT.Helpers.active import get_active_chats
from AMBOTMusicBoT.Helpers.inline import close_key


@app.on_message(filters.command("activevc") & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("𝗧𝗩 𝙂𝙚𝙩𝙩𝙞𝙣𝙜 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝙤𝙞𝙘𝙚𝘾𝙝𝙖𝙩𝙨 𝙇𝙞𝙨𝙩.... ☘")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "𝙋𝙧𝙞𝙫𝙖𝙩𝙚 𝘾𝙝𝙖𝙩 "
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("🦊𝙉𝙤 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝙞𝙙𝙚𝙤 𝘾𝙝𝙖𝙩 𝙊𝙣 𝙈𝙪𝙨𝙞𝙘𝘽𝙤𝙩.🦊")
    else:
        await mystic.edit_text(
            f"**𝙇𝙞𝙨𝙩 𝙤𝙛 𝘾𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩 𝙊𝙣 𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩  :**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )
