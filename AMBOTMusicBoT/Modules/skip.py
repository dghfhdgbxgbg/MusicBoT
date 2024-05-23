

from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio

from AMBOTMusicBoT import BOT_USERNAME, app, AM, pytgcalls
from AMBOTMusicBoT.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb


@app.on_message(filters.command(["skip", "next"]) & filters.group)
@admin_check
async def skip_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    get = AM.get(message.chat.id)
    if not get:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text(
                text=f"𝙎𝙩𝙚𝙖𝙢 𝙎𝙠𝙞𝙥𝙥𝙚𝙙\n│ \n└𝘽𝙮 : {message.from_user.mention} 🥀\n\n**𝙉𝙤 𝙈𝙤𝙧𝙚 𝙌𝙪𝙚𝙪𝙚𝙙 𝙏𝙧𝙖𝙘𝙠𝙨 𝙄𝙣** {message.chat.title}, **𝙇𝙚𝙖𝙫𝙞𝙣𝙜 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩.**",
                reply_markup=close_key,
            )
        except:
            return
    else:
        title = get[0]["title"]
        duration = get[0]["duration"]
        file_path = get[0]["file_path"]
        videoid = get[0]["videoid"]
        req_by = get[0]["req"]
        user_id = get[0]["user_id"]
        get.pop(0)

        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.change_stream(
                message.chat.id,
                stream,
            )
        except:
            await _clear_(message.chat.id)
            return await pytgcalls.leave_group_call(message.chat.id)

        await message.reply_text(
            text=f"𝙎𝙩𝙚𝙖𝙢 𝙎𝙠𝙞𝙥𝙥𝙚𝙙\n│ \n└𝘽𝙮 : {message.from_user.mention} 🥀",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        return await message.reply_photo(
            photo=img,
            caption=f"**📡 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 💡**\n\n**💡𝙏𝙞𝙩𝙡𝙚:** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n **👤𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝘽𝙮:** {req_by}",
            reply_markup=buttons,
        )
