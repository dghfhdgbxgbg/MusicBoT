

import os
import random

from yt_dlp import YoutubeDL

def cookies():
    cookie_dir = "AMBOTMusicBoT/cookies"
    cookies_files = [f for f in os.listdir(cookie_dir) if f.endswith(".txt")]

    cookie_file = os.path.join(cookie_dir, random.choice(cookies_files))
    return cookie_file


ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "cookiefile": cookies(),
    "prefer_ffmpeg": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}
ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    sin = ydl.extract_info(url, False)
    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    ydl.download([url])
    return x_file
