import pyromod
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import dotenv_values
from pyrogram import Client

from estacao_do_amor.src.handlers import add_handlers, message_scheduler
from estacao_do_amor.src.secret import params_bot

config = dotenv_values(".env")
params_bot = params_bot(config)

app = Client("my_bot", **params_bot)

scheduler = AsyncIOScheduler()

add_handlers(app)
message_scheduler(scheduler, app)

