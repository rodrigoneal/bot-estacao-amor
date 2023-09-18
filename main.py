

from pyrogram import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from dotenv import dotenv_values
from estacao_do_amor.src.secret import params_bot
from estacao_do_amor.src.handlers import add_handlers, message_scheduler


config = dotenv_values(".env")
params_bot = params_bot(config)

app = Client("my_bot", test_mode=True)

scheduler = AsyncIOScheduler()

add_handlers(app)
message_scheduler(scheduler, app)

scheduler.start()
app.run()
