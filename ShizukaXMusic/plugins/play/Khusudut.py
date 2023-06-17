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

@app.on_message(filters.regex("^مايسترو$") & filters.group)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5809896714)
    name = usr.first_name
    user = await client.get_chat(5809896714)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5809896714, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**????**
                    
◉ 𝚄𝚂𝙴𝚁 ↝[{usr.first_name}](https://t.me/{usr.username})

◉ 𝙱𝙸𝙾 ↝ {Bio} """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],               
          ]              
       )              
    )
