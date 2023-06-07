import asyncio
import os
from pyrogram.types import CallbackQuery
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["بوت الحذف","رابط الحذف"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50228546bd85a32fecd6e.jpg",
        caption=f"""**ليه بتحذف ياعمري 🥺🥺🥺**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("بوت الحذف", url=f"https://t.me/LC6BOT"),
            ]
         ]
     )
  )

