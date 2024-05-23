

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from AMBOTMusicBoT import app


@app.on_message(filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("𝙂𝙞𝙫𝙚 𝙎𝙤𝙢𝙚 𝙏𝙚𝙭𝙩 𝙏𝙤 𝙎𝙚𝙖𝙧𝙘𝙝 !")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("💸")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"✨ 𝙏𝙞𝙩𝙡𝙚 : {results[i]['title']}\n"
            text += f"⏱ 𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 : `{results[i]['duration']}`\n"
            text += f"👀 𝙑𝙞𝙚𝙬𝙨 : `{results[i]['views']}`\n"
            text += f"📣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 : {results[i]['channel']}\n"
            text += f"🔗 𝙇𝙞𝙣𝙠 : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❰𝗖𝗹𝗼𝘀𝗲❱ ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
