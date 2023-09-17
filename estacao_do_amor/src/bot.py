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


def main():
    """
    Asynchronously sends a welcome message to new chat members.

    Args:
        Client: The client instance.
        message (Message): The message object containing the new chat members.

    Returns:

    """
    private_chat = "https://t.me/estacaodoamorbot"
    @app.on_message(filters.new_chat_members)
    async def welcome_message(Client, message: Message):
        link = "https://linktr.ee/estacaodoamorpod"
        # Loop para cumprimentar cada novo membro individualmente
        for new_member in message.new_chat_members:
            new_member_name = new_member.first_name
            welcome_text = f"Bem-vindo ao grupo mais apaixonante, {new_member_name}! Aqui está o link da estação do amor {link}"
            await message.reply(welcome_text)

    @app.on_message(filters.command("link"))
    async def link(Client, message: Message):
        link = "https://linktr.ee/estacaodoamorpod"
        await message.reply(link)
    

    async def match_estacao():
        group_id = -4014608746
        members = app.get_chat_members(group_id)
        chat_info = await app.get_chat(group_id)
        users = []
        async for member in members:
                user:User = member.user
                users.append(user)
        for user in users:
            photo = user.photo
            photo.big_file_id
            file_name = f"{user.id}.jpg"
            teste = await app.download_media(photo.big_file_id, file_name=file_name)
            user.foto = teste

        create_match(users[0], users[1])
        file_name = open_browser()
        # await app.send_message(chat_info.id,"Esse é o casal mais bonito desse grupo. ")
        await app.send_photo(chat_info.id, file_name, caption="Esse é o casal mais bonito desse grupo. ")

    @app.on_message(filters.command("confesso") & filters.group)
    async def confissao(Client, message: Message):
        mensagem = f"Xiii🤫, eu amo uma confissão, mas não quero que todos fiquem sabendo. Me chame no privado e faça sua confissão. {private_chat}"
        await message.reply(mensagem)

    @app.on_message(filters.command("confesso") & filters.private)
    async def confissao_private(Client, message: Message):
        mensagem = f"Abra seu coração pra mim. \nComece a mensagem escrevendo 'Eu confesso' para eu anotar tudo. Se não quiser dizer seu nome pode ficar tranquila que ninguém vai ficar sabendo."
        await message.reply(mensagem)
    
    @app.on_message(filters.regex(r"(?i)eu confesso") & filters.private)
    async def conficao_message(Client, message: Message):
        if message.from_user and message.from_user.is_bot:
            return
        print(message.text)
        mensagem = "Pode ficar tranquilo que ninguém vai ficar sabendo. É nosso segredinho. 🤐🤐"
        await message.reply(mensagem)


    scheduler = AsyncIOScheduler()
    scheduler.add_job(match_estacao, 'cron', day_of_week='sun', hour=9, minute=33)


    scheduler.start()
    app.run()

