from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import dotenv_values
from .secret import params_bot




config = dotenv_values(".env")
params_bot = params_bot(config)

app = Client(
    "my_bot", test_mode=True, **params_bot
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
    
    @app.on_message(filters.command("confesso") & filters.group)
    async def confissao(Client, message: Message):
        mensagem = f"Xiii🤫, eu amo uma confissão, mas não quero que todos fiquem sabendo. Me chame no privado e faça sua confissão. {private_chat}"
        await message.reply(mensagem)

    @app.on_message(filters.command("confesso") & filters.private)
    async def confissao_private(Client, message: Message):
        mensagem = f"Abra seu coração pra mim. \nComece a mensagem escrevendo 'Eu confesso' para eu anotar tudo. Se não quiser dizer seu nome pode ficar tranquila que ninguém vai ficar sabendo."
        await message.reply(mensagem)
    
    @app.on_message()
    async def conficao_message(Client, message: Message):
        if message.from_user and message.from_user.is_bot:
            return
        confissao = message.text
        trigger = "eu confesso"
        print(confissao)
        if confissao.lower().startswith(trigger):
            mensagem = "Pode ficar tranquilo que ninguém vai ficar sabendo. É nosso segredinho. 🤐🤐"
        else:
            mensagem = "Se for uma confissão, Comece a confissão com 'Eu confesso' para eu anotar tudo. Se não quiser dizer seu nome pode ficar tranquila que ninguém ficara sabendo."
        await message.reply(mensagem)

    app.run()
