
from AMBOTMusicBoT import AM


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = AM.get(chat_id)
    if get:
        AM[chat_id].append(put_f)
    else:
        AM[chat_id] = []
        AM[chat_id].append(put_f)
