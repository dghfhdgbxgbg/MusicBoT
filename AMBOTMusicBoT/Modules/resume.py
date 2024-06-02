from pyrogram import Client, errors, filters
from pyrogram import filters
from pyrogram.types import Message

from AMBOTMusicBoT import app, pytgcalls
from AMBOTMusicBoT.Helpers import admin_check, close_key, is_streaming, stream_on


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
    user_id = callback_query.from_user.id
    if not await admin_check(client, callback_query):
        return await callback_query.answer("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ!", show_alert=True)

    if await is_streaming(chat_id):
        await callback_query.answer("ᴛʜᴇ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ʀᴇꜱᴜᴍᴇᴅ!", show_alert=True)
        return

    await stream_on(chat_id)
    await pytgcalls.resume_stream(chat_id)
    await callback_query.edit_message_text(
        text=f"▶️ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴜᴍᴇ\n│ \n└ʀᴇsᴜᴍᴇᴅ ʙʏ : {callback_query.from_user.mention} 🥀",
        reply_markup=close_key,
    )

    await callback_query.answer("ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʀᴇꜱᴜᴍᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!")
