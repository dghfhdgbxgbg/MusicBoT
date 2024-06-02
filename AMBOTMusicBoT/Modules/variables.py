

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from AMBOTMusicBoT import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>{BOT_NAME} 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀 :</u>

𝘼𝙥𝙞_𝙄𝙙 : <code>{config.API_ID}</code>
𝘼𝙥𝙞_𝙃𝙖𝙨𝙝 : <code>{config.API_HASH}</code>

𝘽𝙤𝙩_𝙏𝙤𝙠𝙚𝙣 : <code>{config.BOT_TOKEN}</code>
𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣_𝙇𝙞𝙢𝙞𝙩𝙨 : <code>{config.DURATION_LIMIT}</code>

𝙊𝙬𝙣𝙚𝙧_𝙄𝙙 : <code>{config.OWNER_ID}</code>
𝙎𝙪𝙙𝙤_𝙐𝙨𝙚𝙧𝙨 : <code>{config.SUDO_USERS}</code>

𝙋𝙞𝙣𝙜_𝙄𝙢𝙜 : <code>{config.PING_IMG}</code>
𝙎𝙩𝙖𝙧𝙩_𝙞𝙢𝙜 : <code>{config.START_IMG}</code>
𝙎𝙪𝙥𝙥𝙤𝙧𝙩_𝘾𝙝𝙖𝙩 : <code>{config.SUPPORT_CHAT}</code>

𝙎𝙚𝙨𝙨𝙞𝙤𝙣 : <code>{config.SESSION}</code>""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝙎𝙚𝙣𝙙 𝙩𝙝𝙚 𝘾𝙤𝙣𝙛𝙞𝙜 𝙑𝙖𝙧𝙞𝙖𝙗𝙡𝙚𝙨.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "𝙋𝙡𝙚𝙖𝙨𝙚 𝘾𝙝𝙚𝙘𝙠 𝙔𝙤𝙪𝙧 𝙋𝙢, 𝙄'𝙫𝙚 𝙎𝙚𝙣𝙩 𝙏𝙝𝙚 𝙘𝙤𝙣𝙛𝙞𝙜 𝙑𝙖𝙧𝙞𝙖𝙗𝙡𝙚𝙨."
        )
