from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import dotenv_values
from pyrogram import Client

from estacao_do_amor.src.domain.repositories.repositories import Repository
from estacao_do_amor.src.handlers import add_handlers, message_scheduler
from estacao_do_amor.src.infra import db
from estacao_do_amor.src.secret import params_bot

config = dotenv_values(".env")
params_bot = params_bot(config)
scheduler = AsyncIOScheduler()


app = Client("my_bot", **params_bot)


# Sei que isso não é uma boa pratica, mas foda-se
app.repository: Repository = Repository(db.async_session_maker)

add_handlers(app)
message_scheduler(scheduler, app)
