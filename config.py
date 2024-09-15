from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN", "6607357754:AAHv3nZdp5aRo-DDXD_QgX9RxrbszwG1fpY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","5810668543"))
EVAL_USERS = list(map(int, getenv("EVAL_USERS", "7137269276 7045191057").split()))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")

SESSION = getenv("SESSION", "BQC6kfsAvhnR04ErG1WMWnmKoaoklAjBeuG_trj-J348ygus4eP0-bV1w4fDqAkfqFF82Fk5tHo5fV67Wd20wRPzwh12iTupUA2Nynivb34_V_R1fDJ-n1ga_oattdPQ3ENdP9mw1QWMug5LFX-PW9c3LhvpBpWkoKozUcXUYwk5vLUeEiDISAahrcZV5YQ8bdFmiPdDg8h8t6eXFGSmBSl3bamBn7MewvIoho26rqlsEaYhvKND8uEAJWX6sgN8H64TYkilGr-13_yNi5wj-FUVbxTdlf-fAXB2d9eGpg5UHJp5mmUHJmeZYNzdpyFSnq4tKedZwk0E6YyZUyhHTn8n5Dh6tQAAAAGZs7ltAA")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TeamSuperBan")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SuperBanSBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7137269276 7045191057").split()))


FAILED = "https://graph.org/file/ba53a21e7a37ffa66694d.jpg"
