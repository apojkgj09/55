import os
import random
import requests
from datetime import datetime
from sys import version_info
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ShizukaXMusic import app
from ShizukaXMusic.utils.decorators.admins import AdminActual
from strings import get_command



disable_cut = []

@app.on_message(filters.regex("^السورس$") & filters.group)
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/1d7c10cf2ad5250c27390.jpg",
        caption=f"""• ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ ʟɪɴᴅᴀ\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ ~ @FH_ME\n• ᴄʜᴀɴɴᴇʟ ʟɪɴᴅᴀ ~ @FH_KP\n**""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                       "𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", user_id=5809896714)
                ],[
                    InlineKeyboardButton(
                        "𝙘𝙝𝙖𝙣𝙣𝙚𝙡 ¹", url=f"https://t.me/FH_KP"), 
                    InlineKeyboardButton(
                        "𝙘𝙝𝙖𝙣𝙣𝙚𝙡 ²", url=f"https://t.me/KB_HE"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك", url=f"https://t.me/LANDHLBOT?startgroup=tru"),
            ]
        ]
         ),
     )
