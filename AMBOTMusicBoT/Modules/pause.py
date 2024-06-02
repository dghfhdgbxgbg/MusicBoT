
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, errors, filters
from AMBOTMusicBoT import app, pytgcalls
from AMBOTMusicBoT import BOT_USERNAME, app, AM, pytgcalls
from AMBOTMusicBoT.Helpers import admin_check, close_key, is_streaming, stream_off
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from AMBOTMusicBoT.Helpers import admin_check, close_key, is_streaming, stream_on
from AMBOTMusicBoT.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb
from AMBOTMusicBoT.Helpers import _clear_, admin_check, close_key

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from AMBOTMusicBoT import BOT_USERNAME

MUSIC = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_stream"),
            InlineKeyboardButton(text="II", callback_data="pause_stream"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_stream"),
            InlineKeyboardButton(text="▢", callback_data="stop_stream"),
        ]
    ]
)

@app.on_message(filters.command(["stop", "end"]) & filters.group)
@admin_check
async def stop_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass

    return await message.reply_text(
        text=f"ᴍᴜꜱɪᴄ ᴇɴᴅᴇᴅ\n│ \n└ʙʏ : {message.from_user.mention} ",
        reply_markup=close_key,
    )


@app.on_callback_query(filters.regex("stop_stream"))
async def stop_stream_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("You don't have the permission to do that!", show_alert=True)

    try:
        await stream_off(chat_id)
        await pytgcalls.leave_group_call(chat_id)
    except Exception as e:
        print(e)

    await callback_query.edit_message_text(
        text=f"ᴍᴜꜱɪᴄ ᴇɴᴅᴇᴅ\n│ \n└ʙʏ : {callback_query.from_user.mention} ",
        reply_markup=close_key,
    )

    await callback_query.answer("Music stopped successfully!")


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
    if not await admin_check(client, callback_query):
        return await callback_query.answer("You don't have the permission to do that!", show_alert=True)

    get = AM.get(chat_id)
    if not get:
        return await callback_query.answer("No tracks queued.", show_alert=True)

    title = get[0]["title"]
    req_by = get[0]["req"]

    get.pop(0)

    stream = AudioPiped(get[0]["file_path"], audio_parameters=HighQualityAudio())
    try:
        await pytgcalls.change_stream(chat_id, stream)
    except Exception as e:
        print(e)
        await _clear_(chat_id)
        return await pytgcalls.leave_group_call(chat_id)

    await callback_query.edit_message_text(
        text=f"Skipped to the next track\n│ \n└️Requested by: {req_by} ",
        reply_markup=close_key,
    )

    await callback_query.answer("Skipped to the next track successfully!")



@app.on_message(filters.command(["resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("𝘿𝙞𝙙 𝙔𝙤𝙪 𝙍𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙏𝙝𝙖𝙩 𝙮𝙤𝙪 𝙋𝙖𝙪𝙨𝙚𝙙 𝙏𝙝𝙚 𝙎𝙩𝙧𝙚𝙖𝙢 ?")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"▶️ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴜᴍᴇ\n│ \n└ʀᴇsᴜᴍᴇᴅ ʙʏ : {message.from_user.mention} 🥀",
        reply_markup=close_key,
    )

@app.on_callback_query(filters.regex("resume_stream"))
async def resume_stream_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("You don't have the permission to do that!", show_alert=True)

    if await is_streaming(chat_id):
        return await callback_query.answer("Music is already playing.")

    await stream_on(chat_id)
    await pytgcalls.resume_stream(chat_id)
    await callback_query.edit_message_text(
        text=f"Music resumed\n│ \n└ʙʏ : {callback_query.from_user.mention} ",
        reply_markup=close_key,
    )

    await callback_query.answer("Music resumed successfully!")


@app.on_message(filters.command(["pause"]) & filters.group)
@admin_check
async def pause_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if not await is_streaming(message.chat.id):
        return await message.reply_text(
            "𝘿𝙞𝙙 𝙔𝙤𝙪 𝙍𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙏𝙝𝙖𝙩 𝙔𝙤𝙪 𝙍𝙚𝙨𝙪𝙢𝙚𝙙 𝙏𝙝𝙚 𝙎𝙩𝙧𝙚𝙖𝙢? "
        )

    await pytgcalls.pause_stream(message.chat.id)
    await stream_off(message.chat.id)
    return await message.reply_text(
        text=f"ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ᴘᴀᴜꜱᴇᴅ\n│ \n└ʙʏ : {message.from_user.mention} ",
        reply_markup=close_key,
    )

@app.on_callback_query(filters.regex("pause_stream"))
async def pause_stream_callback(client: Client, callback_query: CallbackQuery):
    chat_id = callback_query.message.chat.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("You don't have the permission to do that!", show_alert=True)

    if not await is_streaming(chat_id):
        return await callback_query.answer("No music is playing.")

    await pytgcalls.pause_stream(chat_id)
    await stream_off(chat_id)
    await callback_query.edit_message_text(
        text=f"Music paused\n│ \n└ʙʏ : {callback_query.from_user.mention} ",
        reply_markup=close_key,
    )

    await callback_query.answer("Music paused successfully!")
