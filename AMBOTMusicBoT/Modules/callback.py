

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from pytgcalls.types import AudioPiped, HighQualityAudio

from AMBOTMusicBoT import (
    ASS_ID,
    ASS_NAME,
    BOT_ID,
    BOT_MENTION,
    BOT_USERNAME,
    LOGGER,
    app,
    AM,
    pytgcalls,
)
from AMBOTMusicBoT.Helpers import (
    _clear_,
    admin_check_cb,
    gen_thumb,
    is_streaming,
    stream_off,
    stream_on,
)
from AMBOTMusicBoT.Helpers.dossier import *
from AMBOTMusicBoT.Helpers.inline import (
    buttons,
    close_key,
    help_back,
    helpmenu,
    pm_buttons,
)
from AMBOTMusicBoT.Modules.pause import MUSIC

@app.on_callback_query(filters.regex("forceclose"))
async def close_(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "𝙄𝙩'𝙡𝙡 𝙗𝙚 𝘽𝙚𝙩𝙩𝙚𝙧 𝙞𝙛 𝙔𝙤𝙪 𝙎𝙩𝙖𝙮 𝙄𝙣 𝙮𝙤𝙪𝙧 𝙇𝙞𝙢𝙞𝙩𝙨.", show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close"))
async def forceclose_command(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
    except:
        return
    try:
        await CallbackQuery.answer()
    except:
        pass


@app.on_callback_query(filters.regex(pattern=r"^(resume_cb|pause_cb|skip_cb|end_cb)$"))
@admin_check_cb
async def admin_cbs(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass

    data = query.matches[0].group(1)

    if data == "resume_cb":
        if await is_streaming(query.message.chat.id):
            return await query.answer(
                "𝘿𝙞𝙙 𝙮𝙤𝙪 𝙍𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙏𝙝𝙖𝙩 𝙮𝙤𝙪 𝙋𝙖𝙪𝙨𝙚𝙙 𝙩𝙝𝙚 𝙎𝙩𝙧𝙚𝙖𝙢 ?", show_alert=True
            )
        await stream_on(query.message.chat.id)
        await pytgcalls.resume_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙍𝙚𝙨𝙪𝙢𝙚𝙙\n│ \n└𝘽𝙮 : {query.from_user.mention} ",
            reply_markup=close_key,
        )

    elif data == "pause_cb":
        if not await is_streaming(query.message.chat.id):
            return await query.answer(
                "𝘿𝙞𝙙 𝙮𝙤𝙪 𝙍𝙚𝙢𝙚𝙢𝙗𝙚𝙧 𝙏𝙝𝙖𝙩 𝙮𝙤𝙪 𝙍𝙚𝙨𝙪𝙢𝙚𝙙 𝙩𝙝𝙚 𝙎𝙩𝙧𝙚𝙖𝙢 ?", show_alert=True
            )
        await stream_off(query.message.chat.id)
        await pytgcalls.pause_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙋𝙖𝙪𝙨𝙚𝙙 \n│ \n└𝘽𝙮 : {query.from_user.mention} ",
            reply_markup=close_key,
        )

    elif data == "end_cb":
        try:
            await _clear_(query.message.chat.id)
            await pytgcalls.leave_group_call(query.message.chat.id)
        except:
            pass
        await query.message.reply_text(
            text=f"➻ 𝙎𝙩𝙧𝙚𝙖𝙢 𝙀𝙣𝙙𝙚𝙙/𝙎𝙩𝙤𝙥𝙥𝙚𝙙  \n│ \n└𝘽𝙮 : {query.from_user.mention} ",
            reply_markup=close_key,
        )
        await query.message.delete()

    elif data == "skip_cb":
        get = AM.get(query.message.chat.id)
        if not get:
            try:
                await _clear_(query.message.chat.id)
                await pytgcalls.leave_group_call(query.message.chat.id)
                await query.message.reply_text(
                    text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙎𝙠𝙞𝙥𝙥𝙚𝙙\n│ \n└𝘽𝙮 : {query.from_user.mention} \n\n**𝙉𝙤 𝙈𝙤𝙧𝙚 𝙌𝙪𝙚𝙪𝙚𝙙 𝙏𝙧𝙖𝙘𝙠𝙨 𝙞𝙣** {query.message.chat.title}, **𝙡𝙚𝙖𝙫𝙞𝙣𝙜 𝙑𝙞𝙙𝙚𝙤𝙘𝙝𝙖𝙩.**",
                    reply_markup=close_key,
                )
                return await query.message.delete()
            except:
                return
        else:
            title = get[0]["title"]
            duration = get[0]["duration"]
            videoid = get[0]["videoid"]
            file_path = get[0]["file_path"]
            req_by = get[0]["req"]
            user_id = get[0]["user_id"]
            get.pop(0)

            stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
            try:
                await pytgcalls.change_stream(
                    query.message.chat.id,
                    stream,
                )
            except Exception as ex:
                LOGGER.error(ex)
                await _clear_(query.message.chat.id)
                return await pytgcalls.leave_group_call(query.message.chat.id)

            img = await gen_thumb(videoid, user_id)
            await query.edit_message_text(
                text=f"𝙎𝙩𝙧𝙚𝙖𝙢 𝙎𝙠𝙞𝙥𝙥𝙚𝙙\n│ \n└𝘽𝙮 : {query.from_user.mention} ",
                reply_markup=close_key,
            )
            return await query.message.reply_photo(
                photo=img,
                caption=f"**📡 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 💡**\n\n‣ **💡𝙏𝙞𝙩𝙡𝙚 :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n ***👤𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙙 𝘽𝙮 :** {req_by}",
                reply_markup=MUSIC,
            )


@app.on_callback_query(filters.regex("unban_ass"))
async def unban_ass(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id, user_id = callback_request.split("|")
    umm = (await app.get_chat_member(int(chat_id), BOT_ID)).privileges
    if umm.can_restrict_members:
        try:
            await app.unban_chat_member(int(chat_id), ASS_ID)
        except:
            return await CallbackQuery.answer(
                "𝙁𝙖𝙞𝙡𝙚𝙙 𝙩𝙤 𝙐𝙣𝙗𝙖𝙣 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩.",
                show_alert=True,
            )
        return await CallbackQuery.edit_message_text(
            f" {ASS_NAME} 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙐𝙣𝙗𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 {CallbackQuery.from_user.mention}.\n\nᴛʀʏ ᴘʟᴀʏɪɴɢ ɴᴏᴡ..."
        )
    else:
        return await CallbackQuery.answer(
            "𝘿𝙤𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙐𝙣𝙗𝙖𝙣 𝙐𝙨𝙚𝙧𝙨 𝙄𝙣 𝙏𝙝𝙞𝙨 𝘾𝙝𝙖𝙩.",
            show_alert=True,
        )


@app.on_callback_query(filters.regex("AMBOT_help"))
async def help_menu(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass

    try:
        await query.edit_message_text(
            text=f" 𝙃𝙚𝙮 {query.from_user.first_name},\n\n 𝙋𝙡𝙚𝙖𝙨𝙚 𝘾𝙡𝙞𝙘𝙠 𝙊𝙣 𝙩𝙝𝙚 𝘽𝙪𝙩𝙩𝙤𝙣 𝘽𝙚𝙡𝙤𝙬 𝙁𝙤𝙧 𝙒𝙝𝙞𝙘𝙝 𝙔𝙤𝙪 𝙒𝙖𝙣𝙣𝙖 𝙂𝙚𝙩 𝙃𝙚𝙡𝙥.",
            reply_markup=InlineKeyboardMarkup(helpmenu),
        )
    except Exception as e:
        LOGGER.error(e)
        return


@app.on_callback_query(filters.regex("AMBOT_cb"))
async def open_hmenu(_, query: CallbackQuery):
    callback_data = query.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(help_back)

    try:
        await query.answer()
    except:
        pass

    if cb == "help":
        await query.edit_message_text(HELP_TEXT, reply_markup=keyboard)
    elif cb == "sudo":
        await query.edit_message_text(HELP_SUDO, reply_markup=keyboard)
    elif cb == "owner":
        await query.edit_message_text(HELP_DEV, reply_markup=keyboard)
    elif cb == "copy":
        await query.edit_message_text(COPY_DEV, reply_markup=keyboard)


@app.on_callback_query(filters.regex("AMBOT_Home"))
async def home_AMBOT(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass
    try:
        await query.edit_message_text(
            text=PM_START_TEXT.format(
                query.from_user.first_name,
                BOT_MENTION,
            ),
            reply_markup=InlineKeyboardMarkup(pm_buttons),
        )
    except:
        pass
