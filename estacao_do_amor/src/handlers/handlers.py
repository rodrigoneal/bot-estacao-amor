from pyrogram import enums
from pyrogram.client import Client
from pyrogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, Voice

from pyrogram.enums import MessageMediaType

# TODO criar os comandos de correio do amor e sugestão.

link_tree = "https://linktr.ee/estacaodoamorpod"
estacao_id = -4014608746
private_chat = "https://t.me/estacaodoamorbot"
id_audio_ucrania = (
    "CQACAgEAAxkBAAIB2mUJ4QuXi-163DNzX0Mb1L2eoiWQAAK2AwACjGtQRIJkvxo6kCVvHgQ"
)
ricardo_financas_insta = "https://www.instagram.com/ricardoso.financas"
MessageMediaType.VOICE
teclado_personalizado = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton("Sim"), KeyboardButton("Não")]],
    resize_keyboard=True,
    is_persistent=False,
    one_time_keyboard=True,
    placeholder="Escolha uma opção",
)


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


async def command_start_handler(client: Client, message: Message):
    mensagem = (
        "**Bem-vindo ao bot do podcast mais apaixonante do mundo!😍😍**\n\n"
        "Aqui estão algumas opções para interagir conosco:\n\n"
        "/confesso: Se você quiser compartilhar uma confissão e me conte essa fofoca😱.\n\n"
        "/correio: Se você deseja enviar uma mensagem no estilo 'correio do amor' e abra seu coração para o seu amor 💌.\n\n"
        "/link: Para obter o link para ouvir e seguir a Estação do Amor 🎙.\n\n"
        "/sugestao: Se você tiver alguma sugestão ou desejar fazer uma reclamação. Pode hablar 🗣\n\n"
        "/cerveja: Se quiser convidar a gente para beber a resposta é sempre **SIM** 🍻.\n\n"
        "Muito amor pra você, __lindx__ 💋"
    )
    await message.reply(mensagem, parse_mode=enums.ParseMode.MARKDOWN)


async def command_link_handler(Client: Client, message: Message):
    await message.reply(link_tree)


async def command_help_handler(client: Client, message: Message):
    mensagem = (
        "É a sua primeira vez aqui? Fique tranquilo, estou aqui para te guiar com carinho e ensinar você como funciona.\n"
        f"Se você quiser fazer uma confissão, compartilhar uma sugestão ou enviar uma mensagem cheia de amor, basta me chamar na nossa conversa particular [Apaixonado Bot]({private_chat})! \n"
        "E se estiver procurando o link para o podcast mais apaixonante do mundo, é só digitar /link e você poderá nos ouvir sussurrar nos seus ouvidinhos."
    )
    await message.reply(mensagem, parse_mode=enums.ParseMode.MARKDOWN)


async def command_parceiria_handler(client: Client, message: Message):
    await message.reply(
        (
            "Nossa missão é ajudar você a realizar seus sonhos através de uma abordagem cuidadosamente planejada com investimentos estratégicos."
            f"Conte conosco para transformar suas metas em realidade! \n [Ricardo Finanças]({ricardo_financas_insta})"
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


async def command_correio_handler(Client: Client, message: Message):
    answer = await message.chat.ask(
        "Então o cupido flechou esse coraçãozinho!💘... Vai lá abra seu coração e não esqueça de dizer quem é o dono dessa mensagem e desse coração."
    )
    if answer.audio or answer.voice:
        await Client.send_audio(
            message.chat.id,
            id_audio_ucrania,
            duration=6,
        )
        return
    await message.reply(
        "Obrigado por compartilhar conosco! 🤗 Vamos espalhar esse amor para o mundo inteiro. ❤️🔥❤️🔥❤️"
    )


async def command_confesso_group_handler(client: Client, message: Message):
    await message.reply(
        f"Xiii🤫, eu amo uma confissão, mas não quero que todos fiquem sabendo. Me chame no privado e faça sua confissao. {private_chat}"
    )


async def command_confesso_private_handler(client: Client, message: Message):
    if message.from_user and message.from_user.is_bot:
        return
    answer = await message.chat.ask(
        "Conte logo essa fofoca! Só não mande áudios que eu não sou nenhuma safada pra ficar ouvindo áudios"
    )
    confissao = answer.text
    anonimo = await message.chat.ask(
        f"Menina, Isso é bafão! Eu posso falar isso no podcast? ",
        reply_markup=teclado_personalizado,
    )
    if anonimo.text == "Não":
        resposta = "Pra que me conta a fofoca se eu não posso espalhar?😔, mas vou respeitar e venha sempre contar fofoca pra mim."
    else:
        resposta = "Melhor do que ouvir fofoca é contar a fofoca.😈 Ouça o podcast para ouvir a gente espalhar esse bafão."
    await message.reply(resposta)


async def audio_voice_handler(Client: Client, message: Message):
    await message.reply("Opa! Começou o podcast! 🎙")
    await Client.send_audio(
        message.chat.id,
        id_audio_ucrania,
        duration=6,
        caption="Não mande áudios que eu não sou nenhuma safada pra ficar ouvindo áudios",
    )


async def picture_handler(Client: Client, message: Message):
    await message.reply(
        "Você parece ter se confundido de aplicativo; estamos usando o Telegram aqui, enquanto o aplicativo para compartilhamento de fotos é o Instagram!"
    )


async def command_correio_group_handler(client: Client, message: Message):
    await message.reply(
        f"Você não pretende revelar seu amor diante de todos, certo? Me convide para uma conversa privada e compartilhe comigo quem é o(a) sortudo(a). {private_chat}"
    )
