

from AMBOTMusicBoT import AM
from AMBOTMusicBoT.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        AM[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
