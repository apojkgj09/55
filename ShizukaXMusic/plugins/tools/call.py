import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils.database import get_assistant

@app.on_message(filters.voice_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "**تـم فتـح المحـادثه الصـوتيه**"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "**تـم إغـلاق المحـادثه الصـوتيه**"
      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
import asyncio

from pyrogram import Client, filters

from strings import get_command


from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded

from ShizukaXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

from ShizukaXMusic.core.call import Shizuka

from ShizukaXMusic.utils.database import get_assistant

@app.on_message(filters.voice_chat_started)

async def stcall(client: Client, message: Message): 

      Startt = "**تم فتـح المحـادثه الصـونيه**"

      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)

async def encall(client: Client, message: Message): 

      Enddd = "**تـم إغـلاق المحـادثه الصوتيه**"

      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)

async def zoharyy(client: Client, message: Message): 

           text = f"- قام {message.from_user.mention}\n - بدعوة : "

           x = 0

           for user in message.voice_chat_members_invited.users:

             try:

               text += f"[{user.first_name}](tg://user?id={user.id}) "

               x += 1

             except Exception:

               pass

           try:

             await message.reply(f"{text} ")

           except:

             pass
