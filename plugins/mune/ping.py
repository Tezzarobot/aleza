"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
from pyrogram import Client, filters
from info import (
    COMMAND_HAND_LER
)
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "𝖧𝖾𝗒 , 𝖨 𝖺𝗆 𝖠𝗅𝗂𝗏𝖾.𝖳𝗁𝖺𝗇𝗄𝗌 𝖳𝗈 TG-V4MP1R3,DKBOTx ."
HELP = "CAACAgUAAxkBAAEEnY9icR7IVu4XCWIu8b5hmdkWqMSHowACSgUAAkHZ6VUXoTLB53NQIiQE"
# -- Constants End -- #


@Client.on_message(
    filters.command(["alive", "start"], COMMAND_HAND_LER) &
    f_onw_fliter
)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("hi", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_sticker(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
