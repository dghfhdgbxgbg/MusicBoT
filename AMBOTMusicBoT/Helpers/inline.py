
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

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="❌", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="👑", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="💌", url=config.SUPPORT_CHAT),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="🆘", callback_data="AMBOT_help")],
    [
        InlineKeyboardButton(text="🦠", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💌", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="👑", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇꜱ", url=f"https://t.me/About_AMBot"),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="🤖",
            callback_data="AMBOT_cb help",
        ),

        InlineKeyboardButton(text="🔴", callback_data="AMBOT_cb sudo"),
    ],    
    [
        InlineKeyboardButton(
            text="👑",
            callback_data="AMBOT_cb owner",
        ),

        InlineKeyboardButton(text="©️", callback_data="AMBOT_cb copy"),
    ],  
    [   InlineKeyboardButton(text="ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇꜱ", url=f"https://t.me/About_AMBot"),
    ],
    [
        InlineKeyboardButton(text="🔙", callback_data="AMBOT_Home"),
        InlineKeyboardButton(text="❌", callback_data="close"),
    ],
]


help_back = [
 [
        InlineKeyboardButton(text="🔙", callback_data="AMBOT_help"),
        InlineKeyboardButton(text="❌", callback_data="close"),
    ],
]
