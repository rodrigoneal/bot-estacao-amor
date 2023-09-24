import traceback

from pyrogram import enums
from pyrogram.client import Client
from pyrogram.types import CallbackQuery, Message

from estacao_do_amor.src import CONSTANTS, love_bot_responses
from estacao_do_amor.src.domain.schemas.correio_schema import Correio
from estacao_do_amor.src.domain.usecases import correio_usecase
from estacao_do_amor.src.handlers.keyboard import (
    create_option_keyboard,
)

teclado = create_option_keyboard(["Sim", "Não"])

async def testando(name):
    stack = traceback.extract_stack()
    func_name = [s.name for s in stack if s.name.endswith("handler")]
    breakpoint()

    pass

async def new_member_handler(Client: Client, message: Message):
    # Loop para cumprimentar cada novo membro individualmente
    for new_member in message.new_chat_members:
        new_member_name = new_member.first_name
        welcome_text = love_bot_responses.new_member_welcome_response.format(
            member_name=new_member_name, link_tree=CONSTANTS.LINK_TREE
        )
        await message.reply(welcome_text, parse_mode=enums.ParseMode.MARKDOWN)
        await message.reply(
            love_bot_responses.explained_bot_new_member_response
        )


async def left_member_handler(Client: Client, message: Message):
    await message.reply("Parece que o amor não venceu! 😔")


async def command_start_handler(Client: Client, message: Message):
    command = love_bot_responses.start_response
    await message.reply(command, parse_mode=enums.ParseMode.MARKDOWN)


async def command_link_handler(Client: Client, message: Message):
    await message.reply(CONSTANTS.LINK_TREE)


async def command_help_handler(Client: Client, message: Message):
    await message.reply(
        love_bot_responses.help_response.format(
            private_chat=CONSTANTS.PRIVATE_CHAT
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


async def command_partner_handler(Client: Client, message: Message):
    await message.reply(
        love_bot_responses.partner_response.format(
            link_patner=CONSTANTS.LINK_PATNER
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


async def command_correio_handler(Client: Client, message: Message):
    remetente = None
    await message.reply(love_bot_responses.correio_first_respose)
    destinatario = await message.chat.ask(
        (
            "Para quem você quer enviar"
            " o correio do amor? Fala o nome do(a) sortudo(a) 👩‍❤️‍👨 💌"
        )
    )
    identificar = await message.reply(
        "Deseja se identificar? 🤔",
        reply_markup=teclado,
    )
    response = await identificar.wait_for_click(alert="Deseja se identificar?")

    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "Sim":
        nome_response = await message.reply(
            f"Deseja usar o nome {message.chat.first_name}? 🤔",
            reply_markup=teclado,
        )
        resposta = await nome_response.wait_for_click()
        await resposta.message.edit_text(
            f"{resposta.message.text} = {resposta.data}"
        )
        if resposta.data == "Sim":
            remetente = message.chat.first_name
        else:
            nome = await message.chat.ask("Escreva seu nome")
            remetente = nome.text

    mensagem = await message.chat.ask(
        (
            "Agora deixe seu coração"
            " falar e escreva tudo o que sente por essa pessoa. 🤗"
        )
    )

    correio = Correio(
        destinatario=destinatario.text,
        remetente=remetente,
        mensagem=mensagem.text,
    )
    await correio_usecase.create(
        repository=Client.repository.correio_repository, correio_schema=correio
    )
    await message.reply(
        (
            "Obrigado por compartilhar"
            " conosco! 🤗 Vamos espalhar esse"
            " amor para o mundo inteiro. ❤️🔥❤️🔥❤️"
        )
    )


async def command_confesso_group_handler(Client: Client, message: Message):
    await message.reply(
        (
            "Xiii🤫, eu amo uma confissão, "
            "mas não quero que todos fiquem sabendo. "
            "Me chame no privado"
            f" e faça sua confissao. {CONSTANTS.PRIVATE_CHAT}"
        )
    )


async def command_confesso_private_handler(Client: Client, message: Message):
    await testando(__spec__.name)
    if message.from_user and message.from_user.is_bot:
        return
    await message.chat.ask(
        (
            "Conte logo essa fofoca!\n"
            "OBS: Só não mande áudios"
            " que eu não sou nenhuma safada pra ficar ouvindo áudios"
        )
    )
    anonimo = await message.reply(
        "Menina, Isso é bafão! Eu posso falar isso no podcast? ",
        reply_markup=teclado,
    )

    response = await anonimo.wait_for_click()
    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "Não":
        resposta = (
            "Pra que me conta a fofoca se eu não posso espalhar?😔,"
            " mas vou respeitar e venha sempre contar fofoca pra mim."
        )
    else:
        resposta = (
            "Melhor do que ouvir fofoca é contar a fofoca.😈"
            " Ouça o podcast para ouvir a gente espalhar esse bafão."
        )
    await message.reply(resposta)


async def audio_voice_handler(Client: Client, message: Message):
    await message.reply("Opa! Começou o podcast! 🎙")
    await message.reply_voice(
        "estacao_do_amor/media/ucrania.mp3",
        caption=(
            "Não mande áudios que eu não sou"
            " nenhuma safada pra ficar ouvindo áudios"
        ),
        duration=6,
        quote=True,
    )


async def picture_handler(Client: Client, message: Message):
    await Client.send_audio(
        message.chat.id,
        CONSTANTS.ID_PHOTO_NAO_MANDA_FOTO,
        caption="Conhece aquela dupla sertaneja NemVi e NemVerei? 😂",
    )


async def command_correio_group_handler(Client: Client, message: Message):
    await message.reply(
        love_bot_responses.correio_response.format(
            private_chat=CONSTANTS.PRIVATE_CHAT
        )
    )


async def command_cerveja_handle(Client: Client, message: Message):
    await message.chat.ask(love_bot_responses.cerveja_date_response)
    await message.reply(love_bot_responses.cerveja_response)
    await Client.send_venue(
        message.chat.id,
        **CONSTANTS.LOCATION_PARQUE_MADUREIRA,
        title="Parque Madureira",
        address="Rio de Janeiro",
    )


async def command_contact_handler(Client: Client, message: Message):
    await message.reply(
        love_bot_responses.contact_response.format(
            email_estacao=CONSTANTS.ESTACAO_EMAIL
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )
    await message.reply(
        love_bot_responses.contact_member_instagram.format(
            david_instagram=CONSTANTS.DAVID_INSTAGRAM,
            rodrigo_instagram=CONSTANTS.RODRIGO_INSTAGRAM,
            thauan_instagram=CONSTANTS.THAUAN_INSTAGRAM,
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


async def handle_callback_query(client, query: CallbackQuery):
    data = query.data
    await query.message.reply(data)
