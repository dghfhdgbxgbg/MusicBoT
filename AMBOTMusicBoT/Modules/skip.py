
from pyrogram import Client, errors, filters
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery

from AMBOTMusicBoT import BOT_USERNAME, app, AM, pytgcalls
from AMBOTMusicBoT.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb, MUSIC


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
                text=f"ᴍᴜsɪᴄ ꜱᴋɪᴘᴇᴅ\n│ \n└ʙʏ : {message.from_user.mention} 🥀\n\nɴᴏ ᴍᴏʀᴇ Qᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋꜱ ɪɴ {message.chat.title}, ʟᴇᴀᴠɪɴɢ  ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.",
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
            text=f"ᴍᴜsɪᴄ ꜱᴋɪᴘᴇᴅ\n│ \n└ʙʏ : {message.from_user.mention} 🥀",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        return await message.reply_photo(
            photo=img,
            caption=f"📡 ꜱᴛᴀʀᴛᴇᴅ ꜱᴛʀᴇᴀᴍɪɴɢ 💡\n\n💡ᴛɪᴛʟᴇ : [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n 👤ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ: {req_by}",
            reply_markup=MUSIC,
        )

@app.on_callback_query(filters.regex("skip_stream"))
async def skip_stream_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)

    get = AM.get(chat_id)
    if not get:
        try:
            await _clear_(chat_id)
            await pytgcalls.leave_group_call(chat_id)
            await callback_query.message.edit_text(
                text=f"ᴍᴜsɪᴄ ꜱᴋɪᴘᴇᴅ\n│ \n└ʙʏ : {callback_query.from_user.mention} 🥀\n\nɴᴏ ᴍᴏʀᴇ Qᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋꜱ ɪɴ {callback_query.message.chat.title}, ʟᴇᴀᴠɪɴɢ  ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.",
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
                chat_id,
                stream,
            )
        except:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)

        await callback_query.message.edit_text(
            text=f"ᴍᴜsɪᴄ ꜱᴋɪᴘᴇᴅ \n│ \n└ʙʏ : {callback_query.from_user.mention} 🥀",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        await callback_query.message.reply_photo(
            photo=img,
            caption=f"📡 ꜱᴛᴀʀᴛᴇᴅ ꜱᴛʀᴇᴀᴍɪɴɢ💡\n\n💡ᴛɪᴛʟᴇ : [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n 👤ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ: {req_by}",
            reply_markup=MUSIC,
        )

        await callback_query.answer("ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ꜱᴋɪᴘᴘᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!")
