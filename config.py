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

API_ID = int(environ.get("API_ID", "20945078"))
API_HASH = environ.get("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")
BOT_TOKEN = environ.get("BOT_TOKEN", "6716433698:AAHv56l8-VjZ0xHukfL-VTD0vCVWZu64fEU")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002057338886"))
ADMINS = int(environ.get("ADMINS", "1664376941"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ChatGPT:MrGiBIGHgICj70T8@chatgpt.0hmjve1.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "ChatGPT")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
