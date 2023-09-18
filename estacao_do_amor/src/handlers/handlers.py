from pyrogram.types import Message
from pyrogram.client import Client

from pyrogram import enums

link_tree = "https://linktr.ee/estacaodoamorpod"
estacao_id = -4014608746
private_chat = "https://t.me/estacaodoamorbot"


async def new_member_handler(Client: Client, message: Message):
    # Loop para cumprimentar cada novo membro individualmente
    for new_member in message.new_chat_members:
        new_member_name = new_member.first_name
        welcome_text = f"Bem-vindo ao grupo mais apaixonante, {new_member_name}! Clique aqui para o link da estação do amor [Estação do Amor]({link_tree})"
        await message.reply(welcome_text, parse_mode=enums.ParseMode.MARKDOWN)
        await message.reply(
            (
                "Além disso, estamos abertos para receber suas sugestões ou críticas construtivas. Você também pode compartilhar suas confissões mais profundas ou enviar uma mensagem apaixonada no estilo 'correio do amor'."
                "Se tiver alguma dúvida, basta digitar /help, e estaremos prontos para guiá-lo e ajudá-lo a aproveitar ao máximo o bot."
            )
        )


async def command_link_handler(Client: Client, message: Message):
    await message.reply(link_tree)


async def command_confesso_group_handler(client: Client, message: Message):
    await message.reply(
        f"Xiii🤫, eu amo uma confissão, mas não quero que todos fiquem sabendo. Me chame no privado e faça sua confissao. {private_chat}"
    )


async def command_confesso_private_handler(client: Client, message: Message):
    if message.from_user and message.from_user.is_bot:
        return
    await message.reply(
        "Agora esse é nosso segredinho! A gente não salva o nome de quem mandou, mas a gente pode ler no podcast"
    )


async def command_start_handler(client: Client, message: Message):
    mensagem = (
        "Bem-vindo ao bot do podcast mais apaixonante do mundo!\n"
        "Aqui estão algumas opções para interagir conosco:\n"
        "**Confissões**: Se você quiser compartilhar uma confissão, comece sua mensagem com 'eu confesso', e ela será mantida anônima.\n"
        "**Correio do Amor**: Se você deseja enviar uma mensagem no estilo 'correio do amor', inicie sua mensagem com 'correio do amor' e não se esqueça de incluir os nomes de quem envia e para quem se destina.\n"
        "**Link da Estação do Amor**: Digite /link para obter o link direto para a nossa Estação do Amor.\n"
        "**Sugestões e Reclamações**: Se você tiver alguma sugestão ou desejar fazer uma reclamação, comece sua mensagem com 'sugestão' para nos informar.\n"
        "Muito amor pra você, __lindx__ 💋"
    )
    await message.reply(mensagem, parse_mode=enums.ParseMode.MARKDOWN)


async def command_help_handler(client: Client, message: Message):
    mensagem = (
        "É a sua primeira vez aqui? Fique tranquilo, estou aqui para te guiar com carinho e ensinar você como funciona.\n"
        f"Se você quiser fazer uma confissão, compartilhar uma sugestão ou enviar uma mensagem cheia de amor, basta me chamar na nossa conversa particular [Apaixonado Bot]({private_chat})! \n"
        "E se estiver procurando o link para o podcast mais apaixonante do mundo, é só digitar /link e você poderá nos ouvir sussurrar nos seus ouvidinhos."
    )
    await message.reply(mensagem, parse_mode=enums.ParseMode.MARKDOWN)
