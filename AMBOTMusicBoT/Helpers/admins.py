

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from AMBOTMusicBoT import SUDOERS, app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("🤔𝘽𝙤𝙩 𝙞𝙨 𝙉𝙤𝙩 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙊𝙣 𝙑𝙞𝙙𝙚𝙤𝙘𝙝𝙖𝙩🤔")

        if message.from_user.id in SUDOERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "😄𝙔𝙤𝙪'𝙖𝙧𝙚 𝙉𝙤𝙩 𝘼𝙣 MiHRK 𝘼𝙙𝙢𝙞𝙣, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙩𝙖𝙮 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙇𝙞𝙢𝙞𝙩𝙨.😄"
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "😏𝙔𝙤𝙪 𝘿𝙤𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩𝙨, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙩𝙖𝙮 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙇𝙞𝙢𝙞𝙩𝙨😔"
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "🥺𝘽𝙤𝙩 𝙞𝙨 𝙉𝙤𝙩 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙊𝙣 𝙑𝙞𝙙𝙚𝙤𝙘𝙝𝙖𝙩🥺", show_alert=True
            )

        if query.from_user.id in SUDOERS:
            return await func(_, query)

        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "😄𝙔𝙤𝙪'𝙖𝙧𝙚 𝙉𝙤𝙩 𝘼𝙣 MiHRK 𝘼𝙙𝙢𝙞𝙣, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙩𝙖𝙮 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙇𝙞𝙢𝙞𝙩𝙨.😄",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "😏𝙔𝙤𝙪 𝘿𝙤𝙣'𝙩 𝙃𝙖𝙫𝙚 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙑𝙞𝙙𝙚𝙤𝘾𝙝𝙖𝙩𝙨, 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙩𝙖𝙮 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙇𝙞𝙢𝙞𝙩𝙨😔",
                show_alert=True,
            )

    return cb_non_admin
