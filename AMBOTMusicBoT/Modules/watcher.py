from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio, Update

from AMBOTMusicBoT import BOT_ID, BOT_USERNAME, app, app2, AM, pytgcalls
from AMBOTMusicBoT.Helpers import _clear_, buttons, gen_thumb
from AMBOTMusicBoT.Modules.pause import MUSIC
welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass


@app.on_message(filters.left_chat_member)
async def ub_leave(_, message: Message):
    if message.left_chat_member.id == BOT_ID:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
        except:
            pass
        try:
            await app2.leave_chat(message.chat.id)
        except:
            pass


@pytgcalls.on_left()
@pytgcalls.on_kicked()
@pytgcalls.on_closed_voice_chat()
async def swr_handler(_, chat_id: int):
    try:
        await _clear_(chat_id)
    except:
        pass


@pytgcalls.on_stream_end()
async def on_stream_end(pytgcalls, update: Update):
    chat_id = update.chat_id

    get = AM.get(chat_id)
    if not get:
        try:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)
        except:
            return
    else:
        process = await app.send_message(
            chat_id=chat_id,
            text="𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 𝙉𝙚𝙭𝙩 𝙏𝙧𝙖𝙘𝙠 𝙁𝙧𝙤𝙢 𝙌𝙪𝙚𝙪𝙚 🎬...",
        )
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
                chat_id,
                stream,
            )
        except:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)

        img = await gen_thumb(videoid, user_id)
        await process.delete()
        await app.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=f"**📡 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 💡**\n\n**💡𝙏𝙞𝙩𝙡𝙚:** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n**👤𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝘽𝙮:** {req_by}",
            reply_markup=MUSIC,
        )
