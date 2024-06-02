
from pyrogram import Client, errors, filters
from pyrogram import filters
from pyrogram.types import Message

from AMBOTMusicBoT import app, pytgcalls
from AMBOTMusicBoT.Helpers import _clear_, admin_check, close_key


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
    user_id = callback_query.from_user.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)

    try:
        await _clear_(chat_id)
        await pytgcalls.leave_group_call(chat_id)
    except:
        pass

    await callback_query.edit_message_text(
        text=f"ᴍᴜꜱɪᴄ ᴇɴᴅᴇᴅ\n│ \n└ʙʏ : {callback_query.from_user.mention} ",
        reply_markup=close_key,
    )

    await callback_query.answer("ᴍᴜꜱɪᴄ ꜱᴛᴏᴘᴘᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!")
