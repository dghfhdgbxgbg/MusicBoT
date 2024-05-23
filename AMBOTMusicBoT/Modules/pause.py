
from pyrogram import filters
from pyrogram.types import Message

from AMBOTMusicBoT import app, pytgcalls
from AMBOTMusicBoT.Helpers import admin_check, close_key, is_streaming, stream_off


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
        text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙋𝙖𝙪𝙨𝙚𝙙\n│ \n└𝘽𝙮 : {message.from_user.mention} ",
        reply_markup=close_key,
    )
