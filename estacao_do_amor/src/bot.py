from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import dotenv_values

from estacao_do_amor.src.match.estacao_match import create_match
from estacao_do_amor.src.match.take_image import open_browser
from .secret import params_bot
from pyrogram.types.user_and_chats.user import User




config = dotenv_values(".env")
params_bot = params_bot(config)

app = Client(
    "my_bot", test_mode=True
)




