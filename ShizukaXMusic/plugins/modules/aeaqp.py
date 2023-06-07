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



@app.on_message(filters.command(["السورس","سورس"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/343e5269a0d64c31f60b1.jpg",
        caption=f"""♡ 𝙬𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 𝙢𝙪𝙨𝙞𝙘
╭──── • ◈ • ────╮
 [𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 ¹](t.me/FH_3B)
 [𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 ²](t.me/SA_YRAN)
 [𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 ](t.me/KB_HE)
╰──── • ◈ • ────╯""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧", url=f"https://t.me/FHK_M5"),
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
 