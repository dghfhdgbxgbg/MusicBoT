
import asyncio

import speedtest
from pyrogram import filters

from AMBOTMusicBoT import SUDOERS, app


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩...**")
        test.download()
        m = m.edit("**𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝙐𝙥𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**𝙎𝙝𝙖𝙧𝙞𝙣𝙜 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝙍𝙚𝙨𝙪𝙡𝙩𝙨...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "spt"]) & SUDOERS)
async def speedtest_function(_, message):
    m = await message.reply_text("**𝙍𝙪𝙣𝙣𝙞𝙣𝙜 𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**𝙎𝙥𝙚𝙚𝙙𝙏𝙚𝙨𝙩 𝙍𝙚𝙨𝙪𝙡𝙩𝙨** ✯
    
<u>**❥͜͡𝗖𝗹𝗶𝗲𝗻𝘁 :**</u>
**❁ __𝙄𝙨𝙥 :__** {result['client']['isp']}
**❁ __𝘾𝙤𝙪𝙣𝙩𝙧𝙮 :__** {result['client']['country']}
  
<u>**❥͜͡𝗦𝗲𝗿𝘃𝗲𝗿 :**</u>
**❁ __𝙉𝙖𝙢𝙚 :__** {result['server']['name']}
**❁ __𝘾𝙤𝙪𝙣𝙩𝙧𝙮 :__** {result['server']['country']}, {result['server']['cc']}
**❁ __𝙎𝙥𝙤𝙣𝙨𝙤𝙧 :__** {result['server']['sponsor']}
**❁ __𝙇𝙖𝙩𝙚𝙣𝙘𝙮 :__** {result['server']['latency']}  
**❁ __𝙋𝙞𝙣𝙜 :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
