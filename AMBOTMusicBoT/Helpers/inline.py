

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from AMBOTMusicBoT import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="❰𝗖𝗹𝗼𝘀𝗲❱", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="❰𝙂𝙧𝙤𝙪𝙥❱", url=config.SUPPORT_CHAT),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="❰𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨❱", callback_data="AMBOT_help")],
    [
        InlineKeyboardButton(text="❰𝗖𝗵𝗮𝗻𝗻𝗲𝗹❱", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="❰𝗚𝗿𝗼𝘂𝗽❱", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="❰𝙊𝙬𝙣𝙚𝙧❱", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="𝗔𝗱𝗱 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆", url=f"https://github.com/Technical-Robot/TV_Play_Bot"),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="𝘽𝙤𝙩𝙪𝙨𝙚𝙧",
            callback_data="AMBOT_cb help",
        ),

        InlineKeyboardButton(text="𝙎𝙪𝙙𝙤𝙪𝙨𝙚𝙧", callback_data="AMBOT_cb sudo"),
    ],    
    [   InlineKeyboardButton(text="⚡ 𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆 ⚡", url=f"https://github.com/Technical-Robot/TV_Play_Bot"),
    ],
    [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="AMBOT_Home"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
    ],
]


help_back = [
 [
        InlineKeyboardButton(text="𝗕𝗮𝗰𝗸", callback_data="AMBOT_help"),
        InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲", callback_data="close"),
    ],
]
