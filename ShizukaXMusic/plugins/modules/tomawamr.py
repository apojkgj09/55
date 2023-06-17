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



@app.on_message(filters.command(["الاوامر","اوامرليندا"],""))
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/83e32e660ae5b21d3f851.mp4",
        caption=f""" اهلين فيك في اوامر بوت ليندا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "طريقة التفعيل البوت", callback_data=f"gg"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"g1"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"g2"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("hmaya"))
async def bhr(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f""" اهلين فيك في اوامر بوت ليندا 🎶\n\n -› **جميع اوامر البوت موجودة بالاسفل**\n\n• = » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)""",reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "طريقة تفعيل البوت", callback_data=f"gg"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"g1"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"g2"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[
                    InlineKeyboardButton(
                        "إغـلاق", callback_data=f"close"),

                ],
            ]
        ),
    )
@app.on_callback_query(filters.regex("g1"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في المجموعه**
        
**اليك قائـمة الاوامــر 👇**
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**""",
       reply_markup=InlineKeyboardMarkup(
        [
            [                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
            ]
        ]
         ),
     )
@app.on_callback_query(filters.regex("g2"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القناه**


- لتشغيل اغنيه اكتب : /cplay
- لتشغيل فيديو اكتب : /cvideo
- لأنهاء الاغنيه اكتب : /cstop
- لايقاف الاغنيه مؤقت اكتب : /cpause
- لتكملة الاغنيه من الايقاف المؤقت اكتب :/cresume
- لتخطي الاغنيه اكتب : /cskip
- لكتم البوت في الكول اكتب : /cmute
- لألغاء كتم البوت في الكول اكتب : /cunmute""",
       reply_markup=InlineKeyboardMarkup(
        [
            [                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
            ]
        ]
         ),
     )
@app.on_callback_query(filters.regex("cha"))
async def ddd(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""ٓاهلـين حبـي  أليـك قائمة اوامـر التشغيل في القناه**    

» خطوات تشغيل في القناه

» لتشغيل في قناتك

‌‏« قم بانشاء جروب مربوط بقناتك

» تقوم باضافة البوت في القناتك و مجموعتك وترفعه مشرف

» لربط القناتك بالمجموعه ارسل  الامر التالي في المجموعة
            
» /channelplay + معرف قناتك

» /channelplay @FH_KP مثـل**..

» **للاستفسار** » @FH_KN""",
       reply_markup=InlineKeyboardMarkup(
        [
            [                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
            ]
        ]
         ),
     )
@app.on_callback_query(filters.regex("don"))
async def br(_, query: CallbackQuery):
   await query.edit_message_caption(caption =f"""اهليـن فيك  في قسـم التحميـل
•**ا\nللبحث عن اغنية او تحميلها استخدم الامر التالي ↓\n\n[ بحث + اسم المطلوب ..]\n\nمثل » بحث وحشتيني**""",
        reply_markup=InlineKeyboardMarkup(
        [
            [                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
            ]
        ]
         ),
     )
@app.on_callback_query(filters.regex("gg"))
async def devmusic(_, query: CallbackQuery):
   await query.edit_message_text(
        f"""**طريقة تفعيل البوت في مجموعتك :**
1.) **اولا قم بإضافة البوت اللي مجموعتك \n√.**
2.) **قم برفع البوت مشرف مع الصلاحيات المطلوبة \n√.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر \n√.**
4.) **تاكد من تشغيل المحادثة الصوتية\n√.**
5.) ** اكتب شغل او تشغيل + اسم الاغنية \n√.**
▪️ ** في حال لم يستطع الحساب المساعد الانضمام إلى مجموعتك قم باضافتة يدوي\n√.**
\n√ **في حال واجهت اي مشكلة اخري يمكنك التواصل معي : @FH_ME **
\n __ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙡𝙞𝙣𝙙𝙖 [ᴄʜᴀɴɴᴇʟ](https://t.me/KB_HE)""",
        reply_markup=InlineKeyboardMarkup(
        [
            [                    
                    InlineKeyboardButton(
                        "رجـوع 🎶", callback_data=f"hmaya"),
            ]
        ]
         ),
     )
 
