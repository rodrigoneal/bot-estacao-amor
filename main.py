import asyncio

from config import app, scheduler
from estacao_do_amor.src.infra.db import create_tables

loop = asyncio.get_event_loop()

loop.run_until_complete(create_tables())
scheduler.start()
print("BOT INICIADO")
app.run()
