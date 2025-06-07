import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "22215080"))
API_HASH = environ.get("API_HASH", "6ab80ad5d78fee18fdd9b909edfbafd5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002344280987"))
ADMINS = int(environ.get("ADMINS", "7841292070"))
DB_URI = environ.get("DB_URI", "mongodb+srv://meenakanhaiyalal638:files@files.8ko8k.mongodb.net/?retryWrites=true&w=majority&appName=files")
DB_NAME = environ.get("DB_NAME", "ChatGPT")
OPENAI_API = environ.get("OPENAI_API", "AIzaSyBHT9Tv3pyB0xwOKJzGvv1MYi6bvpSwRtA")
AI = is_enabled((environ.get("AI","True")), False)
