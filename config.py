from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN", "6712019543:AAGTLOS-HqNNCM3OrMaN4Swmg0TPqgcS6xo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","7045191057"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")

SESSION = getenv("SESSION", "BACpEosuO9iutpRGyAlqKV6YF785FE5VLFcbUQxo-M-YJUykeu6oxvzpVjr5iNcchKzQUec9L1YQpRWxPnNw9tHXKnLpCLiWoFlK9HuI2_PvTXencKFIvq2f4hiupCkgYb_Gb-tGq52qoftRc0Qf4-FVfEIwn5-q702qO5v1r6PvQHL5cndUly8CRsHqy5Lf9nHj0ss9Y_3k25GmAIEZy9pV3GwK5tN5m8z87ZL5JnpIRHAth6r7_jwdRI7d5N7npBFSKK3Jft8WuLq76yqoBswcLndq1fq8d6a9I-I91bL9Y-ysFpZGRL0teI0kjEQNpHcik55YdU-4AJfqEg4tY2huAAAAAYQ-mekA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6531494164 7045191057").split()))


FAILED = "https://graph.org/file/ba53a21e7a37ffa66694d.jpg"
