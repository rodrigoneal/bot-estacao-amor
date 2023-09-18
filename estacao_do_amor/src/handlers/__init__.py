from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from . import handlers
from.schedules_handlers import generate_match

from apscheduler.schedulers.asyncio import AsyncIOScheduler


def add_handlers(app: Client) -> None:
    app.add_handler(MessageHandler(handlers.new_member_handler, filters.new_chat_members))
    app.add_handler(MessageHandler(handlers.command_link_handler, filters.command("link")))
    app.add_handler(MessageHandler(handlers.command_start_handler, filters.command("start")))
    app.add_handler(MessageHandler(handlers.command_help_handler, filters.command("help")))
    app.add_handler(MessageHandler(handlers.command_confesso_group_handler, filters.command("confesso") & filters.group))
    app.add_handler(MessageHandler(handlers.command_confesso_private_handler, filters.regex(r"(?i)eu confesso") & filters.private))

def message_scheduler(scheduler: AsyncIOScheduler, app: Client) -> None:
    scheduler.add_job(generate_match, 'cron', day_of_week='mon', hour=18, minute=55, kwargs={"Client": app, "message": None})