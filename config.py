from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN", "7297995696:AAFkm-89e2KFdq_KvRRDT4wJtasv4JEHASo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID","7045191057"))
EVAL_USERS = list(map(int, getenv("EVAL_USERS", "7137269276 7045191057").split()))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/ba53a21e7a37ffa66694d.jpg")

SESSION = getenv("SESSION", "BQAyhNx5cuC4k_CuuNXAOsmbVsijhzjUBujpHYZdIDNR4Aw8wC-8xubyRyt2Wfv2q_dp1UofhkSrkLv5pAtaRHgxXmpRU6g3jhS4dwP6u66sryUh0WTgrrBnQonjAbAL1XsZsqnbQ1J4dynCv1YdZB3u4brAnMhyNuZdBBb3h6GQ3bMRVUkoyEh54NVWQsb92yJJkoHlRP9yAasM0mGum33A27gvgUUpy-8GQDGUTeVK0dBojQEKhqDevKxNxO9xLHVk46eMBKhD7aeTGDDXtH_2F2Ve7WqJSl1eXS_2VDcxlOCP5Av7mFUxdNoXuGsa9QCIgDoGFAt7BHGTF0G-26iYAAAAAYfbFdoA")

bot = os.getenv('bot', 'BQARa_AYNH1-d6BrmrJTRhqiHXH5rafSM7MzHs1xHDKHIAjCc-XWPyCec29-C71j-Xf1PLNoHmkcbrmR5Pyee-6dTATHNf5QhZ4KwHrXTkVS2zvlFzb5Cj5ib6QYbYBNb-Zap1hQsGGNiGVnlw9FTzIbQWG6Hv2B46nUl5yNedmrqz8cIiUzCGkPdC2EW9OqHUzY6xi5Y47Q3ClEAkQvb9GEMxQYafZ5Yi7XxwIdYCYJbPzhDsEll7AM0nTF63xRUVGtD7fGZOy-SIawKQKU2dPCzlPX3ufcjTgtfXN4xhHSfMOeoC7RZb-o2Q9Lp2GugVdpRL6nBeNYrkUgMNbBjwuxAAAAAWVeGzQA')
bot2 = os.getenv('bot2', 'BQALP4Oem21VSasVIL-p-jlR8ccSxQexgsVziw4J7joxtbzI1kTtjS2rYcNFdC8ksyJ8UGJAR1GpDXFPhrIhiR2LEPwBqJ_-BXt0AQhnhBc26voEitcCc2OJoqTZaF8vkNkPdCaRCAq1GfH4oq3hPChwN_7Wtp1MAO8IEHLlCoKDeZarSFInLFlcVmEW9YaE8pH-ULiholf7boNljw4xcUrO3el0RHMCCi1FmmOonHWwR6l6nvbj5XMduKc844YGsitOsPop78TPlauKTjJpAeyn59HF4WPGYn6FnP57I9RZwLRIyBzK9rn34rSqvyjUNQiSASkUaKtC9_V_7HIXzgdEAAAAAVVfK6AA')

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TeamSuperBan")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SuperBanSBots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6531494164 7045191057").split()))


FAILED = "https://graph.org/file/ba53a21e7a37ffa66694d.jpg"
