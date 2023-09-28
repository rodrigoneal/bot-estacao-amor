from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, filters
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from . import automation_handlers, handlers, schedules_handlers


def add_handlers(app: Client) -> None:
    # Handlers para quando entra ou sai um membro
    app.add_handler(
        MessageHandler(handlers.new_member_handler, filters.new_chat_members)
    )
    app.add_handler(
        MessageHandler(handlers.left_member_handler, filters.left_chat_member)
    )
    # Handlers para quando envia um comando
    app.add_handler(
        MessageHandler(
            handlers.command_start_handler, filters.command("start")
        )
    )
    app.add_handler(
        MessageHandler(handlers.command_link_handler, filters.command("link"))
    )
    app.add_handler(
        MessageHandler(handlers.command_help_handler, filters.command("help"))
    )
    app.add_handler(
        MessageHandler(
            handlers.command_partner_handler, filters.command("parceiros")
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_correio_group_handler,
            filters.command("correio") & filters.group,
        )
    )
    

    app.add_handler(
        MessageHandler(
            handlers.command_correio_handler,
            filters.command("correio") & filters.private,
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_confesso_group_handler,
            filters.command("confesso") & filters.group,
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_confesso_private_handler,
            filters.command("confesso") & filters.private,
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_cerveja_handle, filters.command("cerveja")
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_contact_handler, filters.command("contato")
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_feedback_handler,
            filters.command("feedback") & filters.private,
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_feedback_handler_group,
            filters.command("feedback") & filters.group,
        )
    )
    app.add_handler(
        MessageHandler(
            handlers.command_commands_handler, filters.command("comandos")
        )
    )

    app.add_handler(
        MessageHandler(
            handlers.ver_relatos_handler,
            filters.command("relatorio") & (filters.user(907947267) | filters.user(1378479345) | filters.user(6429186104) & filters.private), 
        )
    )

    # Handlers para quando envia um algo que o bot não entende
    app.add_handler(
        MessageHandler(
            handlers.audio_voice_handler, filters.audio | filters.voice
        )
    )
    app.add_handler(
        MessageHandler(handlers.picture_handler, filters.photo | filters.video)
    )

    # Handlers automatizar o podcast
    app.add_handler(
        MessageHandler(
            automation_handlers.create_youtube_video, filters.command("video")
        )
    )

    # Callbacks
    app.add_handler(CallbackQueryHandler(handlers.handle_callback_query))


def message_scheduler(scheduler: AsyncIOScheduler, app: Client) -> None:
    # scheduler.add_job(
    #     schedules_handlers.generate_match,
    #     "cron",
    #     day_of_week=1,
    #     hour=0,
    #     minute=42,
    #     kwargs={"Client": app},
    # )

    scheduler.add_job(
        schedules_handlers.last_episode,
        "cron",
        day_of_week=1,
        hour=12,
        minute=00,
        kwargs={"Client": app},
    )
    pass
