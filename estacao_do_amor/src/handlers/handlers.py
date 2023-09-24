from pyrogram import enums
from pyrogram.client import Client
from pyrogram.types import CallbackQuery, Message

from estacao_do_amor.src import CONSTANTS, love_bot_responses
from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.domain.repositories.correio_repository import (
    CorreioRepository,
)
from estacao_do_amor.src.domain.schemas.correio_schema import Correio
from estacao_do_amor.src.domain.usecases import correio_usecase

from estacao_do_amor.src.handlers.util import handler_bot


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


@handler_bot
async def command_correio_handler(
    Client: Client,
    message: Message,
    repository: CorreioRepository,
    utter_message: UtterMessage,
):
    remetente = None
    await message.reply(love_bot_responses.correio_first_respose)
    destinatario = await message.chat.ask(
        utter_message["utter_boas_vindas_correio"].text
    )
    identificar_response = utter_message["utter_identicar_correio"]
    identificar = await message.reply(
        identificar_response.text,
        reply_markup=identificar_response.keyboard,
    )
    response = await identificar.wait_for_click(alert="Deseja se identificar?")

    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "aceito":
        mudar_nome = utter_message["utter_escolher_nome_correio"]
        nome_response = await message.reply(
            mudar_nome.text.format(name=message.chat.first_name),
            reply_markup=mudar_nome.keyboard,
        )
        response = await nome_response.wait_for_click()
        await response.message.edit_text(
            f"{response.message.text} = {response.data}"
        )
        if response.data == "aceito":
            remetente = message.chat.first_name
        else:
            nome = await message.chat.ask("Escreva seu nome")
            remetente = nome.text

    mensagem = await message.chat.ask(
        utter_message["utter_escreva_mensagem_correio"].text
    )

    correio = Correio(
        destinatario=destinatario.text,
        remetente=remetente,
        mensagem=mensagem.text,
    )
    await correio_usecase.create(repository=repository, correio_schema=correio)
    await message.reply(
        utter_message["utter_agradecendo_correio"].text,
    )


@handler_bot
async def command_confesso_group_handler(
    Client: Client,
    message: Message,
    utter_message: UtterMessage,
):
    await message.reply(
        utter_message["utter_confesso_group"].text.format(
            private_chat=CONSTANTS.PRIVATE_CHAT
        )
    )


@handler_bot
async def command_confesso_private_handler(
    Client: Client,
    message: Message,
    repository: CorreioRepository,
    utter_message: UtterMessage,
):
    if message.from_user and message.from_user.is_bot:
        return
    await message.chat.ask(utter_message["utter_boas_vindas_confesso"].text)
    utter_fofoca = utter_message["utter_surpresa_confesso"]
    anonimo = await message.reply(
        utter_fofoca.text,
        reply_markup=utter_fofoca.keyboard,
    )
    response = await anonimo.wait_for_click()
    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "rejeitado":
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
