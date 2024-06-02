

import platform
import re
import socket
import uuid
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls.__version__ import __version__ as pytgver

from AMBOTMusicBoT import BOT_NAME, SUDOERS, app
from AMBOTMusicBoT.Modules import ALL_MODULES


@app.on_message(filters.command(["stats", "sysstats"]) & SUDOERS)
async def sys_stats(_, message: Message):
    sysrep = await message.reply_text(
        f"𝙂𝙚𝙩𝙩𝙞𝙣𝙜 {BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨, 𝙄𝙩'𝙡𝙡 𝙏𝙖𝙠𝙚 𝘼 𝙒𝙝𝙞𝙡𝙚..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.03))) + " 𝙂𝘽"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}𝙂𝙃𝙕"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}𝙈𝙃𝙕"
    except:
        cpu_freq = "𝗙𝗮𝗶𝗹𝗲𝗱 𝗧𝗼 𝗙𝗲𝘁𝗰𝗵"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.03)
    total = str(total)
    used = hdd.used / (1024.03)
    used = str(used)
    free = hdd.free / (1024.03)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➜ <u>{BOT_NAME} 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨</u>

𝙋𝙮𝙩𝙝𝙤𝙣 : <code>{pyver.split()[0]}</code>
𝙋𝙧𝙤𝙜𝙧𝙖𝙢 : <code>{pyrover}</code>
𝙋𝙮-𝙏𝙜𝙘𝙖𝙡𝙡𝙨 : <code>{pytgver}</code>
𝙎𝙪𝙙𝙤𝙚𝙧𝙨 : <code>{sudoers}</code>
𝙈𝙤𝙙𝙪𝙡𝙚𝙨 : <code>{mod}</code>

𝙄𝙋 : <code>{ip_address}</code>
𝙈𝙖𝙘 : <code>{mac_address}</code>
𝙃𝙤𝙨𝙩𝙣𝙖𝙢𝙚 : <code>{hostname}</code>
𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 : <code>{sp}</code>
𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙤𝙧 : <code>{processor}</code>
𝘼𝙧𝙘𝙝𝙞𝙩𝙚𝙘𝙩𝙪𝙧𝙚 : <code>{architecture}</code>
𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 𝙍𝙚𝙡𝙚𝙖𝙨𝙚 : <code>{platform_release}</code>
𝙋𝙡𝙖𝙩𝙛𝙤𝙧𝙢 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 : <code>{platform_version}</code>

        <b><u>𝗦𝘁𝗼𝗿𝗮𝗴𝗲</b><u/>
𝘼𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚 : <code>{total[:4]}</code> 𝙂𝙞𝙗
𝙐𝙨𝙚𝙙 : <code>{used[:4]}</code> 𝙂𝙞𝙗
𝙁𝙧𝙚𝙚 : <code>{free[:4]}</code> 𝙂𝙞𝙗

𝙍𝙖𝙢 : <code>{ram}</code>
𝙋𝙝𝙮𝙨𝙞𝙘𝙖𝙡 𝘾𝙤𝙧𝙚𝙨 : <code>{p_core}</code>
𝙏𝙤𝙩𝙖𝙡 𝘾𝙤𝙧𝙚𝙨 : <code>{t_core}</code>
𝘾𝙥𝙪 𝙁𝙧𝙚𝙦𝙪𝙚𝙣𝙘𝙮  : <code>{cpu_freq}</code>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❌",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )
