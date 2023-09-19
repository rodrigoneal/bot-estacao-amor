from pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from pyrogram.client import Client
from pyrogram import enums

# TODO criar os comandos de correio do amor e sugestão.

link_tree = "https://linktr.ee/estacaodoamorpod"
estacao_id = -4014608746
private_chat = "https://t.me/estacaodoamorbot"


teclado_personalizado = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("Sim"), KeyboardButton("Não")]
        ],
        resize_keyboard=True,
        is_persistent=False,
        one_time_keyboard=True,
        placeholder="Escolha uma opção"
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


async def command_link_handler(Client: Client, message: Message):
    await message.reply(link_tree)


async def command_confesso_group_handler(client: Client, message: Message):
    await message.reply(
        f"Xiii🤫, eu amo uma confissão, mas não quero que todos fiquem sabendo. Me chame no privado e faça sua confissao. {private_chat}"
    )



async def command_confesso_private_handler(client: Client, message: Message):
    if message.from_user and message.from_user.is_bot:
        return
    answer = await message.chat.ask("Conte logo essa fofoca! Só não mande áudios que eu não sou nenhuma safada pra ficar ouvindo áudios")
    confissao = answer.text
    anonimo = await message.chat.ask(f'Menina, Isso é bafão! Eu posso falar isso no podcast? ', reply_markup=teclado_personalizado)
    if anonimo.text == "Não":
        resposta = "Pra que me conta a fofoca se eu não posso espalhar?😔, mas vou respeitar e venha sempre contar fofoca pra mim."
    else:  
        resposta = "Melhor do que ouvir fofoca é contar a fofoca.😈 Ouça o podcast para ouvir a gente espalhar esse bafão."
    await message.reply(resposta)


async def command_start_handler(client: Client, message: Message):
    mensagem = (
        "Bem-vindo ao bot do podcast mais apaixonante do mundo!😍😍\n"
        "Aqui estão algumas opções para interagir conosco:\n"
        "**Confissões**: Se você quiser compartilhar uma confissão, envie **/confesso** e me conte essa fofoca😱.\n"
        "**Correio do Amor**: Se você deseja enviar uma mensagem no estilo 'correio do amor', **/correio** e abra seu coração para o seu amor 💌.\n"
        "**Link da Estação do Amor**: Digite /link para obter o link direto para a nossa Estação do Amor 🎙.\n"
        "**Sugestões e Reclamações**: Se você tiver alguma sugestão ou desejar fazer uma reclamação, /feedback pode hablar 🗣\n"
        "**Chamar pra beber**: Se quiser convidar a gente para beber pode enviar mensagem direto pra gente e a resposta é sempre **SIM** 🍻.\n"
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
