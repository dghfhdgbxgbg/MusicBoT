

import os

import requests
import yt_dlp
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from AMBOTMusicBoT import BOT_MENTION, BOT_USERNAME, LOGGER, app


@app.on_message(filters.command(["song", "vsong", "video", "music"]))
async def song(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    m = await message.reply_text("🔎")

    query = "".join(" " + str(i) for i in message.command[1:])
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as ex:
        LOGGER.error(ex)
        return await m.edit_text(
            f"𝙁𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝙁𝙚𝙩𝙘𝙝 𝙏𝙧𝙖𝙘𝙠 𝙁𝙧𝙤𝙢 𝙔𝙩-𝘿𝙡.\n\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{ex}`"
        )

    await m.edit_text("𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙎𝙤𝙣𝙜,\n\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"𒀭 **𝙏𝙞𝙩𝙡𝙚 :** [{title[:23]}]({link})\n𒀭 **𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 :** `{duration}`\n𒀭 **𝙐𝙥𝙡𝙤𝙖𝙙𝙚𝙙 𝘽𝙮 :** {BOT_MENTION}"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        try:
            visit_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝙔𝙤𝙪𝙏𝙪𝙗𝙚",
                            url=link,
                        )
                    ]
                ]
            )
            await app.send_audio(
                chat_id=message.from_user.id,
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )
            if message.chat.type != ChatType.PRIVATE:
                await message.reply_text(
                    "𝙋𝙡𝙚𝙖𝙨𝙚 𝘾𝙝𝙚𝙘𝙠 𝙔𝙤𝙪𝙧 𝙋𝙢, 𝙎𝙚𝙣𝙩 𝙏𝙝𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝙎𝙤𝙣𝙜 𝙏𝙝𝙚𝙧𝙚."
                )
        except:
            start_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚",
                            url=f"https://t.me/{BOT_USERNAME}?start",
                        )
                    ]
                ]
            )
            return await m.edit_text(
                text="𝘾𝙡𝙞𝙘𝙠 𝙊𝙣 𝙏𝙝𝙚 𝘽𝙪𝙩𝙩𝙤𝙣 𝘽𝙚𝙡𝙤𝙬 𝘼𝙣𝙙 𝙎𝙩𝙖𝙧𝙩 𝙈𝙚 𝙁𝙤𝙧 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙤𝙣𝙜.",
                reply_markup=start_butt,
            )
        await m.delete()
    except:
        return await m.edit_text("𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝙐𝙥𝙡𝙤𝙖𝙙 𝘼𝙪𝙙𝙞𝙤 𝙊𝙣 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙎𝙚𝙧𝙫𝙚𝙧𝙨.")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as ex:
        LOGGER.error(ex)
