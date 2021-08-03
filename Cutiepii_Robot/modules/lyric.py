from asyncio import get_running_loop
from functools import partial
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent)
from pyrogram import filters

from telegram import Bot, Update, Message, Chat
from telegram.ext import CallbackContext, run_async

from Cutiepii_Robot.modules.helper_funcs.alternate import typing_action
from Cutiepii_Robot import arq, dispatcher, pgram as cutiepii
from Cutiepii_Robot.modules.disable import DisableAbleCommandHandler

@cutiepii.on_message(filters.command("lyrics"))
async def lyrics_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]
    song = await arq.lyrics(query)
    lyrics = song.result
    if len(lyrics) < 4095:
        return await m.edit(f"__{lyrics}__")
    lyrics = await paste(lyrics)
    await m.edit(f"**LYRICS_TOO_LONG:** [URL]({lyrics})")
