import asyncio
from pyrogram import Client, filters, idle
from email.mime.text import MIMEText
from aiosmtplib import send
import os
import random
from datetime import datetime
from time import time
from pyrogram.errors import MessageDeleteForbidden, RPCError
from asyncio import sleep
from pyrogram import Client, enums
from pyrogram.types import Message, User
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
import html
import re
import asyncio
import math
import os
import shlex
from typing import Tuple
from PIL import Image
from pymediainfo import MediaInfo
from functools import partial
from pyrogram.errors import FloodWait, UsernameInvalid
from pyrogram.types import Message
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatType
import asyncio
import os
from os import getenv
import traceback
from pyrogram import filters, Client
from pyrogram.types import Message
from unidecode import unidecode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random 
import time
from config import OWNER_ID, EVAL_USERS
from AMBOTMusicBoT import ASS_MENTION, LOGGER, SUDOERS, app, bot, bot2

smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_user = os.getenv('EMAIL_USER', 'abhibist630@gmail.com')
email_password = os.getenv('EMAIL_PASSWORD', 'waobpkqdfucotcgz')
to_email = 'info@allen.in'

# Additional email accounts
email_user2 = os.getenv('EMAIL_USER2', 'abhimodszyt@gmail.com')
email_password2 = os.getenv('EMAIL_PASSWORD2', 'ebouepnxbhshqwij')

email_user3 = os.getenv('EMAIL_USER3', '9xyzoo@gmail.com')
email_password3 = os.getenv('EMAIL_PASSWORD3', 'askkipnspwyxaudc')

mails = [
    """Hey Allen,

I hope this message finds you well. It has come to our attention that someone is distributing your study material without authorization on a Telegram Group. To protect your intellectual property rights, we urge you to take immediate action to block this Group.

Group URLs: https://t.me/{chat_url}

Infringement Proof Urls:
{message_link}
{message_link2}

Best regards,
Your Students""",
    """Dear Allen,

I trust you're doing well. We've discovered that your study material is being shared on a Telegram Group without your consent. This infringement undermines your hard work and the integrity of your content. Please act swiftly to block this Group to prevent further dissemination.

Group URLs: https://t.me/{chat_url}

Infringement Proof Urls:
{message_link}
{message_link2}

Best regards,
Your Students """,
    """Hi Allen,

I hope this email finds you in good spirits. It has come to our attention that your study material is being circulated on a Telegram Group without your authorization. This poses a threat to the exclusivity of your content. We urge you to take immediate action to block this Group.

Group URLs: https://t.me/{chat_url}

Infringement Proof Urls:
{message_link}
{message_link2}

Best regards,
Your Students""",
    """Dear Allen,

I trust you're well. We regret to inform you that someone is disseminating your study material without permission on a Telegram Group. This constitutes a serious infringement of your intellectual property rights. Please promptly block this Group to protect your content.

Group URLs: https://t.me/{chat_url}

Infringement Proof Urls:
{message_link}
{message_link2}

Best regards,
Your Students""",
    """Hey Allen,

I hope you're having a good day. Unfortunately, we've discovered that your study material is being shared without authorization on a Telegram Group. This is a violation of your intellectual property rights and demands urgent action. Please block this Group to prevent further dissemination.

Group URLs: https://t.me/{chat_url}

Infringement Proof Urls:
{message_link}
{message_link2}

Best,
Your Students""",
]


AM_PIC = [
    "https://graph.org/file/ed513284c18489abfaf5f.jpg",
    "https://graph.org/file/ed513284c18489abfaf5f.jpg",
    
]
ban_txt = """

➻ ʜᴇʟʟᴏ {} ᴛʜɪꜱ ɪꜱ ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ.

➻ ᴛʜɪꜱ ɪꜱ ᴍᴀᴅᴇ ꜰᴏʀ ᴄᴏᴘʏʀɪɢʜᴛ ɢʀᴏᴜᴘꜱ.

ᴘᴏᴡᴇʀ ʙʏ : @SuperBanSBots
"""
help_txt = """
» ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs.
"""
killall_txt = """
1. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /report ᴄᴏᴘʏʀɪɢʜᴛ ꜰʀᴏᴍ ᴍᴇꜱꜱᴇɢᴇꜱ.
2. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /reportpfd ᴄᴏᴘʏʀɪɢʜᴛ ꜰʀᴏᴍ ꜰɪʟᴇ.
3. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /leave ɢɪᴠᴇ ᴍᴇ ᴜꜱᴇʀɴᴀᴍᴇ ᴡʜɪᴄʜ ɢʀᴏᴜᴘ ꜰʀᴏᴍ ʟᴇᴀᴠᴇ.
4. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /setpfp ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
5. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /delpfp ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
6. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /setbio ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
7. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /setname ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
8. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /leaveall1 ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
9. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /leaveall2 ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
10. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /leaveallch1 ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
11. ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴜꜱᴇ ꜰᴏʀᴍᴀᴛ ʟɪᴋᴇ : /leaveallch2 ᴀʙ ᴋʏᴀ ʟɪᴋʜᴜ ᴍᴇ.
"""

app_buttons = [

                [ 
                    InlineKeyboardButton("ᴄᴏᴘʏʀɪɢʜᴛ", callback_data="copyright_"),
        
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]

back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]

button = InlineKeyboardMarkup([
        
        [
            InlineKeyboardButton("ꜱᴜᴘᴇʀʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/SuperBanSBots"),    
        ],
    [
           InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_"),    
      ],
     [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),    
        ],
    
])

@app.on_message(filters.command(["ok"], prefixes=[".","/","!"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=ban_txt.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )    

@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
            InlineKeyboardButton("ꜱᴜᴘᴇʀʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/SuperBanSBots"),    
        ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ban_txt.format(query.from_user.mention, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(app_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="copyright_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                killall_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
            
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
        
   
 
@app.on_message(filters.command(["leave"]) & filters.user(EVAL_USERS))
async def send_pdf(_, message: Message):
        chat_id = message.chat.id
        await message.reply("ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ ᴜꜱᴇʀɴᴀᴍᴇ.")
        response = await app.listen(chat_id)
        chat_url = response.text.strip()
        chat_url = response.text.strip()
        if chat_url.startswith("https://t.me/+"):
           chat_url = chat_url.replace("https://t.me/+", "https://t.me/joinchat/")
        if chat_url.startswith("@"):
           chat_url = chat_url[1:]
        try:
            await bot.leave_chat(chat_url)
            await bot2.leave_chat(chat_url)
            await message.reply(f"ʟᴇᴀᴠᴇ ᴅᴏɴᴇ ꜰʀᴏᴍ : @{chat_url}")
        except Exception as e:
            await message.reply(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ : {e}")
            return
 
@app.on_message(filters.command(["leaveallch1"], prefixes=[".","/","!"]) & filters.private & filters.user(EVAL_USERS))
async def kickmeallch(client: Client, message: Message):
    AMBOT = await edit_or_reply(message, "`Global Leave from channels chats...`")
    er = 0
    done = 0
    async for dialog in bot.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await bot.leave_chat(chat)
            except BaseException:
                er += 1
    await AMBOT.edit(
        f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇxɪᴛ {done} ᴄʜᴀɴɴᴇʟ, ꜰᴀɪʟᴇᴅ ᴛᴏ ᴇxɪᴛ {er} ᴄʜᴀɴɴᴇʟ"
    )

@app.on_message(filters.command(["leaveallch2"], prefixes=[".","/","!"]) & filters.private & filters.user(EVAL_USERS))
async def kickmeallch(client: Client, message: Message):
    AMBOT = await edit_or_reply(message, "`Global Leave from channels chats...`")
    er = 0
    done = 0
    async for dialog in bot2.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await bot2.leave_chat(chat)
            except BaseException:
                er += 1
    await AMBOT.edit(
        f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴇxɪᴛ {done} ᴄʜᴀɴɴᴇʟ, ꜰᴀɪʟᴇᴅ ᴛᴏ ᴇxɪᴛ {er} ᴄʜᴀɴɴᴇʟ"
    )


@app.on_message(filters.command(["leaveall1"], prefixes=[".","/","!"]) & filters.private & filters.user(EVAL_USERS))
async def kickmeall(client: Client, message: Message):
    AMBOT = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in bot2.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await bot2.leave_chat(chat)
            except BaseException:
                er += 1
    await AMBOT.edit(
        f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛ {done} ɢʀᴏᴜᴘ, ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴇꜰᴛ{er} ɢʀᴏᴜᴘ"
    )
    
@app.on_message(filters.command(["leaveall2"], prefixes=[".","/","!"]) & filters.private & filters.user(EVAL_USERS))
async def kickmeall(client: Client, message: Message):
    AMBOT = await edit_or_reply(message, "`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in bot.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await bot.leave_chat(chat)
            except BaseException:
                er += 1
    await AMBOT.edit(
        f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʟᴇꜰᴛ {done} ɢʀᴏᴜᴘ, ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴇꜰᴛ{er} ɢʀᴏᴜᴘ"
    )
   
@app.on_message(filters.command(["report"], prefixes=[".", "/", "!"]) & filters.private)
async def report_command(client: Client, message: Message):
    if message.from_user.id not in EVAL_USERS:
        await message.reply("You don't have authorization to use this command.")
        return
    id = message.chat.id
    await message.reply("ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴄᴏᴘʏʀɪɢʜᴛ @ɢʀᴏᴜᴘᴜꜱᴇʀɴᴀᴍᴇ , ɢʀᴏᴜᴘᴜꜱᴇʀɴᴀᴍᴇ, ɢʀᴏᴜᴘ ɪɴᴠɪᴛᴇʟɪɴᴋ")
    response = await app.listen(id)

    chat_url = response.text.strip()
    if chat_url.startswith("https://t.me/+"):
        chat_url = chat_url.replace("https://t.me/+", "https://t.me/joinchat/")
    if chat_url.startswith("@"):
        chat_url = chat_url[1:]

    try:
        try:
            await bot.get_chat(chat_url)
            already_in_chat = True
        except Exception:
            already_in_chat = False

        if not already_in_chat:
            await bot.join_chat(chat_url)

        try:
            await bot2.get_chat(chat_url)
            already_in_chat_bot2 = True
        except Exception:
            already_in_chat_bot2 = False

        if not already_in_chat_bot2:
            await bot2.join_chat(chat_url)

    except UsernameInvalid:
        await message.reply("ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴜꜱᴇʀɴᴀᴍᴇ ɪꜱ ɪɴᴠᴀʟɪᴅ. ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴄʜᴀᴛ ᴜʀʟ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ.")
        return
    except Exception as e:
        await message.reply(f"​🇫​​🇦​​🇮​​🇱​​🇪​​🇩​ ​🇹​​🇴​ ​🇯​​🇴​​🇮​​🇳​ ​🇹​​🇭​​🇪​ ​🇨​​🇭​​🇦​​🇹​ : {e}")
        return

    messege = """𝘈𝘓𝘓𝘌𝘕 

    2. Stored food of red algae is similar to :- 
    (1) Chitin     (2) Mannitol 

              (3) Amylopectin and glycogen 

    (4) Glycogen and chitin

    3. Complex post fertilization development is seen 
    in which algae ? 
    (1) Green algae      (2) Brown algae 

    (3) Yellow green algae     (4) Red algae
            """
    try:
        sent_message = await bot.send_message(chat_url, messege)
        await asyncio.sleep(120)
        sent_message2 = await bot2.send_message(chat_url, messege)
        await bot.leave_chat(chat_url)
        await bot2.leave_chat(chat_url)
    except Exception as e:
        await message.reply(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴄʜᴀᴛ : {e}")
        return

    try:
        message_id = sent_message.id
        message_id2 = sent_message2.id
        message_link = f"https://t.me/{chat_url}/{message_id}"
        message_link2 = f"https://t.me/{chat_url}/{message_id2}"
        subject = "Infringing Content on Telegram"

        formatted_body = random.choice(mails).format(chat=chat_url, message_link=message_link, message_link2=message_link2)

        await send_email(subject, formatted_body, email_user, email_password, to_email)
        await send_email(subject, formatted_body, email_user2, email_password2, to_email)
        await send_email(subject, formatted_body, email_user3, email_password3, to_email)

        await message.reply(f"ᴛʜᴇ ʀᴇᴘᴏʀᴛ ʜᴀꜱ ʙᴇᴇɴ ꜱᴇɴᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ.\nɢʀᴏᴜᴘ ᴜʀʟꜱ : https://t.me/{chat_url}\nɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ᴘʀᴏᴏꜰ ᴜʀʟꜱ : {message_link}\nɪɴꜰʀɪɴɢᴇᴍᴇɴᴛ ᴘʀᴏᴏꜰ ᴜʀʟꜱ : {message_link2}")
    except Exception as e:
        await message.reply(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ᴘʀᴏᴄᴇꜱꜱ ᴛʜᴇ ʀᴇᴘᴏʀᴛ : {e}")


        
async def send_email(subject, body, email_user, email_password, to_email):
    message = MIMEText(body)
    message['From'] = email_user
    message['To'] = to_email
    message['Subject'] = subject

    try:
        await send(
            message,
            hostname=smtp_server,
            port=smtp_port,
            start_tls=True,
            username=email_user,
            password=email_password
        )
    except Exception as e:
        print(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴇɴᴅ ᴇᴍᴀɪʟ ꜰʀᴏᴍ {email_user}: {e}")


            
@app.on_message(filters.command(["setpfp"]) & filters.user(EVAL_USERS))
async def set_pfp(_, message: Message):
    if message.reply_to_message and message.reply_to_message.photo:
        fuk = await message.reply_text("𝙉𝙤 𝘾𝙝𝙖𝙣𝙜𝙞𝙣𝙜 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘...")
        img = await message.reply_to_message.download()
        await bot.set_profile_photo(photo=img)
        await bot2.set_profile_photo(photo=img)
        return await fuk.edit_text(
            f"» {bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention} 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.."
        )
    else:
        await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙏𝙤 𝘼 𝙋𝙝𝙤𝙩𝙤 𝙁𝙤𝙧 𝘾𝙝𝙖𝙣𝙜𝙞𝙣𝙜 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘."
        )



@app.on_message(filters.command(["delpfp"]) & filters.user(EVAL_USERS))
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in bot.get_chat_photos("me")]
        pfp2 = [p async for p in bot2.get_chat_photos("me")]
        await bot.delete_profile_photos(pfp[0].file_id)
        await bot2.delete_profile_photos(pfp2[0].file_id)
        return await message.reply_text(f"{bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention}𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘." )
    except Exception as e:
        await message.reply_text(f"𝙁𝙖𝙞𝙡𝙚𝙙 𝙏𝙤 𝘿𝙚𝙡𝙚𝙩𝙚 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙋𝙧𝙤𝙛𝙞𝙡𝙚 𝙋𝙞𝙘.: {e}")


@app.on_message(filters.command(["setbio"]) & filters.user(EVAL_USERS))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await bot.update_profile(bio=newbio)
            await bot2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention} 𝘽𝙞𝙤 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await bot.update_profile(bio=newbio)
        await bot2.update_profile(bio=newbio)
        return await message.reply_text(f"» {bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention} 𝘽𝙞𝙤 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.")
    else:
        return await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙏𝙤 𝘼 𝙈𝙖𝙨𝙨𝙖𝙜𝙚 𝙊𝙧 𝙂𝙞𝙫𝙚 𝙎𝙤𝙢𝙚 𝙏𝙚𝙭𝙩 𝙏𝙤 𝙎𝙚𝙩 𝙄𝙩 𝘼𝙨 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝘽𝙞𝙤."
        )


@app.on_message(filters.command(["setname"]) & filters.user(EVAL_USERS))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await bot.update_profile(first_name=name)
            await bot2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention} 𝙉𝙖𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await bot.update_profile(first_name=name, last_name="")
        await bot2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {bot.me.mention} 𝘼𝙣𝙙 {bot2.me.mention} 𝙉𝙖𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮.")
    else:
        return await message.reply_text(
            "𝙍𝙚𝙥𝙡𝙮 𝙩𝙤 𝙖 𝙈𝙖𝙨𝙨𝙖𝙜𝙚 𝙤𝙧 𝙂𝙞𝙫𝙚 𝙎𝙤𝙢𝙚 𝙏𝙚𝙭𝙩 𝙏𝙤 𝙎𝙚𝙩 𝙄𝙩 𝘼𝙨 𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩'𝙨 𝙉𝙚𝙬 𝙉𝙖𝙢𝙚"
        )

            

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


def get_args(message: Message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message
    return list(filter(lambda x: len(x) > 0, split))


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def convert_to_image(message, client) -> [None, str]:
    """Convert Most Media Formats To Raw Image"""
    if not message:
        return None
    if not message.reply_to_message:
        return None
    final_path = None
    if not (
        message.reply_to_message.video
        or message.reply_to_message.photo
        or message.reply_to_message.sticker
        or message.reply_to_message.media
        or message.reply_to_message.animation
        or message.reply_to_message.audio
    ):
        return None
    if message.reply_to_message.photo:
        final_path = await message.reply_to_message.download()
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.mime_type == "image/webp":
            final_path = "webp_to_png_s_proton.png"
            path_s = await message.reply_to_message.download()
            im = Image.open(path_s)
            im.save(final_path, "PNG")
        else:
            path_s = await client.download_media(message.reply_to_message)
            final_path = "lottie_proton.png"
            cmd = (
                f"lottie_convert.py --frame 0 -if lottie -of png {path_s} {final_path}"
            )
            await run_cmd(cmd)
    elif message.reply_to_message.audio:
        thumb = message.reply_to_message.audio.thumbs[0].file_id
        final_path = await client.download_media(thumb)
    elif message.reply_to_message.video or message.reply_to_message.animation:
        final_path = "fetched_thumb.png"
        vid_path = await client.download_media(message.reply_to_message)
        await run_cmd(f"ffmpeg -i {vid_path} -filter:v scale=500:500 -an {final_path}")
    return final_path


def resize_image(image):
    im = Image.open(image)
    maxsize = (512, 512)
    if (im.width and im.height) < 512:
        size1 = im.width
        size2 = im.height
        if im.width > im.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(maxsize)
    file_name = "Sticker.png"
    im.save(file_name, "PNG")
    if os.path.exists(image):
        os.remove(image)
    return file_name


class Media_Info:
    def data(media: str) -> dict:
        "Get downloaded media's information"
        found = False
        media_info = MediaInfo.parse(media)
        for track in media_info.tracks:
            if track.track_type == "Video":
                found = True
                type_ = track.track_type
                format_ = track.format
                duration_1 = track.duration
                other_duration_ = track.other_duration
                duration_2 = (
                    f"{other_duration_[0]} - ({other_duration_[3]})"
                    if other_duration_
                    else None
                )
                pixel_ratio_ = [track.width, track.height]
                aspect_ratio_1 = track.display_aspect_ratio
                other_aspect_ratio_ = track.other_display_aspect_ratio
                aspect_ratio_2 = other_aspect_ratio_[0] if other_aspect_ratio_ else None
                fps_ = track.frame_rate
                fc_ = track.frame_count
                media_size_1 = track.stream_size
                other_media_size_ = track.other_stream_size
                media_size_2 = (
                    [
                        other_media_size_[1],
                        other_media_size_[2],
                        other_media_size_[3],
                        other_media_size_[4],
                    ]
                    if other_media_size_
                    else None
                )

        dict_ = (
            {
                "media_type": type_,
                "format": format_,
                "duration_in_ms": duration_1,
                "duration": duration_2,
                "pixel_sizes": pixel_ratio_,
                "aspect_ratio_in_fraction": aspect_ratio_1,
                "aspect_ratio": aspect_ratio_2,
                "frame_rate": fps_,
                "frame_count": fc_,
                "file_size_in_bytes": media_size_1,
                "file_size": media_size_2,
            }
            if found
            else None
        )
        return dict_


async def resize_media(media: str, video: bool, fast_forward: bool) -> str:
    if video:
        info_ = Media_Info.data(media)
        width = info_["pixel_sizes"][0]
        height = info_["pixel_sizes"][1]
        sec = info_["duration_in_ms"]
        s = round(float(sec)) / 1000

        if height == width:
            height, width = 512, 512
        elif height > width:
            height, width = 512, -1
        elif width > height:
            height, width = -1, 512

        resized_video = f"{media}.webm"
        if fast_forward:
            if s > 3:
                fract_ = 3 / s
                ff_f = round(fract_, 2)
                set_pts_ = ff_f - 0.01 if ff_f > fract_ else ff_f
                cmd_f = f"-filter:v 'setpts={set_pts_}*PTS',scale={width}:{height}"
            else:
                cmd_f = f"-filter:v scale={width}:{height}"
        else:
            cmd_f = f"-filter:v scale={width}:{height}"
        fps_ = float(info_["frame_rate"])
        fps_cmd = "-r 30 " if fps_ > 30 else ""
        cmd = f"ffmpeg -i {media} {cmd_f} -ss 00:00:00 -to 00:00:03 -an -c:v libvpx-vp9 {fps_cmd}-fs 256K {resized_video}"
        _, error, __, ___ = await run_cmd(cmd)
        os.remove(media)
        return resized_video

    image = Image.open(media)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))

    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = "sticker.png"
    image.save(resized_photo)
    os.remove(media)
    return resized_photo
    

def cleanhtml(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = r"\*_`\["
    return re.sub(r"([%s])" % escape_chars, r"\\\1", text)


def mention_html(user_id, name):
    return '<a href="tg://user?id={}">{}</a>'.format(user_id, html.escape(name))


def mention_markdown(user_id, name):
    return "[{}](tg://user?id={})".format(escape_markdown(name), user_id)


async def extract_userid(message, text: str):
    def is_int(text: str):
        try:
            int(text)
        except ValueError:
            return False
        return True

    text = text.strip()

    if is_int(text):
        return int(text)

    entities = message.entities
    app = message._client
    if len(entities) < 2:
        return (await app.get_users(text)).id
    entity = entities[1]
    if entity.type == "mention":
        return (await app.get_users(text)).id
    if entity.type == "text_mention":
        return entity.user.id
    return None


async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def extract_user(message):
    return (await extract_user_and_reason(message))[0]


async def extract_args(message, markdown=True):
    if not (message.text or message.caption):
        return ""

    text = message.text or message.caption

    text = text.markdown if markdown else text
    if " " not in text:
        return ""

    text = sub(r"\s+", " ", text)
    text = text[text.find(" ") :].strip()
    return text


async def extract_args_arr(message, markdown=True):
    return extract_args(message, markdown).split()

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


def GetFromUserID(message: Message):
    """Get the user id of the incoming message."""
    return message.from_user.id


def GetChatID(message: Message):
    """Get the group id of the incoming message"""
    return message.chat.id


def GetUserMentionable(user: User):
    """Get mentionable text of a user."""
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = "<a href='tg://user?id={}'>{}</a>".format(user.id, name_string)

    return username



def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply


