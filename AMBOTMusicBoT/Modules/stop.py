

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
        text=f"**𝙎𝙩𝙚𝙖𝙢 𝙀𝙣𝙙𝙚𝙙/𝙎𝙩𝙤𝙥𝙥𝙚𝙙** \n│ \n└𝘽𝙮 : {message.from_user.mention} ",
        reply_markup=close_key,
    )
