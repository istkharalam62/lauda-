import random
import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from AnieXEricaMusic import app
from AnieXEricaMusic.core.userbot import Userbot
from AnieXEricaMusic.utils.database import delete_served_chat
from AnieXEricaMusic.utils.database import get_assistant

photo = [
    "https://telegra.ph/file/de3b1ab2d139d16656258.jpg",
    "https://telegra.ph/file/bc288c1cfd7ca64d672f0.jpg",
    "https://telegra.ph/file/3a0d9845f6ad4f4ccc11b.jpg",
    "https://telegra.ph/file/f9a03656922e5e16b96d8.jpg",
    "https://telegra.ph/file/f9a03656922e5e16b96d8.jpg",

]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"❍𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ\n\n"
                    f"❍𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}\n"
                    f"❍𝐂ʜᴀᴛ 𝐈ᴅ: {message.chat.id}\n"
                    f"❍𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ: @{username}\n"
                    f"❍𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs: {count}\n"
                    f"❍𝐀ᴅᴅᴇᴅ 𝐁ʏ: {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"❍𝐀ᴅᴅᴇᴅ 𝐁ʏ❍",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
