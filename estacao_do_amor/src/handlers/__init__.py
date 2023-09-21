from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from . import handlers
from. import automation_handlers

from.schedules_handlers import generate_match, last_episode

from apscheduler.schedulers.asyncio import AsyncIOScheduler

estacao_id = -4014608746


def add_handlers(app: Client) -> None:
    app.add_handler(MessageHandler(handlers.new_member_handler, filters.new_chat_members))
    app.add_handler(MessageHandler(handlers.left_member_handler, filters.left_chat_member))
    app.add_handler(MessageHandler(handlers.command_start_handler, filters.command("start")))
    app.add_handler(MessageHandler(handlers.command_link_handler, filters.command("link")))
    app.add_handler(MessageHandler(handlers.command_help_handler, filters.command("help")))
    app.add_handler(MessageHandler(handlers.command_parceiria_handler, filters.command("parceiros")))
    app.add_handler(MessageHandler(handlers.command_correio_group_handler, filters.command("correio") & filters.group))
    app.add_handler(MessageHandler(handlers.command_correio_handler, filters.command("correio") & filters.private))
    app.add_handler(MessageHandler(handlers.command_confesso_group_handler, filters.command("confesso") & filters.group))
    app.add_handler(MessageHandler(handlers.command_confesso_private_handler, filters.command("confesso") & filters.private))
    app.add_handler(MessageHandler(handlers.command_cerveja_handle, filters.command("cerveja")))
    app.add_handler(MessageHandler(handlers.command_contact_handler, filters.command("contato")))
    app.add_handler(MessageHandler(handlers.audio_voice_handler, filters.audio | filters.voice))
    app.add_handler(MessageHandler(handlers.picture_handler, filters.photo | filters.video))
    # Handlers automatizar o podcast
    app.add_handler(MessageHandler(automation_handlers.create_youtube_video, filters.command("video")))

def message_scheduler(scheduler: AsyncIOScheduler, app: Client) -> None:
    scheduler.add_job(generate_match, 'cron', day_of_week=4, hour=19, minute=0, kwargs={"Client": app}) # Envia toda sexta às 19:00 o match dos membros do grupo
    scheduler.add_job(last_episode, 'cron', day_of_week=1, hour=10, minute=30, kwargs={"Client": app}) # Envia o ultimo episodio do podcast todas as terça as 10:30