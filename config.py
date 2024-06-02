from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN", "6712019543:AAGTLOS-HqNNCM3OrMaN4Swmg0TPqgcS6xo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","7045191057"))
EVAL_USERS = list(map(int, getenv("EVAL_USERS", "7137269276 7045191057").split()))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")

SESSION = getenv("SESSION", "BACpEosuO9iutpRGyAlqKV6YF785FE5VLFcbUQxo-M-YJUykeu6oxvzpVjr5iNcchKzQUec9L1YQpRWxPnNw9tHXKnLpCLiWoFlK9HuI2_PvTXencKFIvq2f4hiupCkgYb_Gb-tGq52qoftRc0Qf4-FVfEIwn5-q702qO5v1r6PvQHL5cndUly8CRsHqy5Lf9nHj0ss9Y_3k25GmAIEZy9pV3GwK5tN5m8z87ZL5JnpIRHAth6r7_jwdRI7d5N7npBFSKK3Jft8WuLq76yqoBswcLndq1fq8d6a9I-I91bL9Y-ysFpZGRL0teI0kjEQNpHcik55YdU-4AJfqEg4tY2huAAAAAYQ-mekA")

bot = os.getenv('bot', 'BQARa_AYNH1-d6BrmrJTRhqiHXH5rafSM7MzHs1xHDKHIAjCc-XWPyCec29-C71j-Xf1PLNoHmkcbrmR5Pyee-6dTATHNf5QhZ4KwHrXTkVS2zvlFzb5Cj5ib6QYbYBNb-Zap1hQsGGNiGVnlw9FTzIbQWG6Hv2B46nUl5yNedmrqz8cIiUzCGkPdC2EW9OqHUzY6xi5Y47Q3ClEAkQvb9GEMxQYafZ5Yi7XxwIdYCYJbPzhDsEll7AM0nTF63xRUVGtD7fGZOy-SIawKQKU2dPCzlPX3ufcjTgtfXN4xhHSfMOeoC7RZb-o2Q9Lp2GugVdpRL6nBeNYrkUgMNbBjwuxAAAAAWVeGzQA')
bot2 = os.getenv('bot2', 'BQALP4Oem21VSasVIL-p-jlR8ccSxQexgsVziw4J7joxtbzI1kTtjS2rYcNFdC8ksyJ8UGJAR1GpDXFPhrIhiR2LEPwBqJ_-BXt0AQhnhBc26voEitcCc2OJoqTZaF8vkNkPdCaRCAq1GfH4oq3hPChwN_7Wtp1MAO8IEHLlCoKDeZarSFInLFlcVmEW9YaE8pH-ULiholf7boNljw4xcUrO3el0RHMCCi1FmmOonHWwR6l6nvbj5XMduKc844YGsitOsPop78TPlauKTjJpAeyn59HF4WPGYn6FnP57I9RZwLRIyBzK9rn34rSqvyjUNQiSASkUaKtC9_V_7HIXzgdEAAAAAVVfK6AA')

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AM_YTSUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AMBOTYT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6531494164 7045191057").split()))


FAILED = "https://graph.org/file/ba53a21e7a37ffa66694d.jpg"
