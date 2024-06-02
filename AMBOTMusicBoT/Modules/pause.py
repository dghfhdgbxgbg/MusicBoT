
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, errors, filters
from AMBOTMusicBoT import app, pytgcalls
from AMBOTMusicBoT.Helpers import admin_check, close_key, is_streaming, stream_off
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery


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
    user_id = callback_query.from_user.id

    # Check if the user is an admin
    if not await admin_check(client, callback_query):
        return await callback_query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)

    if not await is_streaming(chat_id):
        await callback_query.answer("The ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴘᴀᴜꜱᴇᴅ!", show_alert=True)
        return

    await pytgcalls.pause_stream(chat_id)
    await stream_off(chat_id)
    await callback_query.edit_message_text(
        text=f"ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ᴘᴀᴜꜱᴇᴅ\n│ \n└ʙʏ : {callback_query.from_user.mention} ",
        reply_markup=close_key,
    )

    await callback_query.answer("ᴍᴜꜱɪᴄ ᴘᴀᴜꜱᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!")
