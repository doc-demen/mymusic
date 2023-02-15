#
# Copyright (C) 2021-2022 byMoni_Help@Github, < https://github.com/mukeshmoni >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Its_me_moni
# Rocks © @Its_me_moni
# Owner moni
# monish
# All rights reserved. © Alisha © Moni © Yukki


from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from ChikkamMusic import app
from ChikkamMusic.core.call import Moni
from ChikkamMusic.utils.database import is_music_playing, music_on
from ChikkamMusic.utils.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@app.on_message(
    filters.command(RESUME_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"], disable_web_page_preview=True)
    await music_on(chat_id)
    await Moni.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )
