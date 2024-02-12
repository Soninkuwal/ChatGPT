from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://graph.org/file/a06ad835b7ddbf1614632.jpg",
        caption="**HELLO** 🇮🇳\n\n**🤖 I AM A CHATGPT BOT 👀**\n\n**🙋 ME HELP FOR ASK ANY QUESTIONS 🗣️\n\n**💕 ❤️ MY FATHER❤️ 💕 kanhaiyalalmeenakuwal\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[KANHAIYA LAL MEENA KUWAL](https://t.me/Chatkanhabot)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Sonickuwalupdate')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/Chatkanhabot'),
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/Sonickuwalupdate')
                    ]
                ]
            )
        )
  
