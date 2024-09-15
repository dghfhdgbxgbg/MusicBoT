
from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from AMBOTMusicBoT import BOT_MENTION, BOT_NAME, app
from AMBOTMusicBoT.Helpers import gp_buttons, pm_buttons
from AMBOTMusicBoT.Helpers.dossier import *
from AMBOTMusicBoT.database.db import *

@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def AMBOT_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **𝗧𝗿𝗮𝗰𝗸 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻** 

📌 **𝙏𝙞𝙩𝙡𝙚 :** {title}

⏳ **𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 :** {duration} 𝙈𝙞𝙣
👀 **𝙑𝙞𝙚𝙬𝙨 :** `{views}`
⏰ **𝙋𝙪𝙗𝙡𝙞𝙨𝙝𝙚𝙙 𝙊𝙣 :** {published}
🔗 **𝙇𝙞𝙣𝙠 :** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})
🎥 **𝘾𝙝𝙖𝙣𝙣𝙚𝙡 :** [{channel}]({channellink})

💖 𝙎𝙚𝙖𝙧𝙘𝙝 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 ⚡︎ {BOT_NAME}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="𝙔𝙤𝙪𝙏𝙪𝙗𝙚", url=link),
                            InlineKeyboardButton(
                                text="𝙂𝙧𝙤𝙪𝙥", url=config.SUPPORT_CHAT
                            ),
                        ],
                    ]
                )
                await m.delete()
                return await app.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            await add_served_user(message.from_user.id)
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_MENTION,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        await add_served_chat(message.chat.id)
        await message.reply_photo(
            photo=config.START_IMG,
            caption=START_TEXT.format(
                message.from_user.first_name,
                BOT_MENTION,
                message.chat.title,
                config.SUPPORT_CHAT,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
