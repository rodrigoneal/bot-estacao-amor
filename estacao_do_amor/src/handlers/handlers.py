from pyrogram import enums
from pyrogram.client import Client
from pyrogram.types import CallbackQuery, Message

from estacao_do_amor.src import constants
from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.domain import usecases
from estacao_do_amor.src.domain.repositories.repositories import Repository
from estacao_do_amor.src.domain.schemas.cerveja_schema import Cerveja
from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso
from estacao_do_amor.src.domain.schemas.correio_schema import Correio
from estacao_do_amor.src.domain.schemas.feedback_schema import FeedBack
from estacao_do_amor.src.handlers.util import handler_bot
from datetime import date


@handler_bot
async def new_member_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    # Loop para cumprimentar cada novo membro individualmente
    for new_member in message.new_chat_members:
        new_member_name = new_member.first_name
        await message.reply(
            utter_message["utter_boas_vindas_new_member"].text.format(
                member_name=new_member_name, link_tree=constants.LINK_TREE
            ),
            parse_mode=enums.ParseMode.MARKDOWN,
        )
        await message.reply(utter_message["utter_explicando_new_member"].text)


@handler_bot
async def left_member_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(utter_message["utter_left_member"].text)


@handler_bot
async def command_start_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_start"].text, parse_mode=enums.ParseMode.MARKDOWN
    )


async def command_link_handler(Client: Client, message: Message):
    await message.reply(constants.LINK_TREE)


@handler_bot
async def command_help_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_help"].text.format(
            private_chat=constants.PRIVATE_CHAT
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


@handler_bot
async def command_partner_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_patner"].text.format(
            link_patner=constants.LINK_PATNER
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


@handler_bot
async def command_correio_handler(
    Client: Client,
    message: Message,
    repository: Repository,
    utter_message: UtterMessage,
):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    remetente = None
    await message.reply(utter_message["utter_first_response_correio"].text)
    destinatario = await message.chat.ask(
        utter_message["utter_boas_vindas_correio"].text
    )
    if destinatario.text == "/cancelar":
        await message.reply(utter_message["utter_cancelar_operacao"].text)
        return
    identificar_response = utter_message["utter_identicar_correio"]

    Client.on_message

    identificar = await message.reply(
        identificar_response.text,
        reply_markup=identificar_response.keyboard,
    )
    response = await identificar.wait_for_click()

    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "/cancelar":
        await message.reply(utter_message["utter_cancelar_operacao"].text)
        return
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
        if response.data == "/cancelar":
            await message.reply(utter_message["utter_cancelar_operacao"].text)
            return

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
        user_id=user_id,
        user_name=user_name,
    )
    await usecases.correio_usecase.create(
        repository=repository.correio_repository, correio_schema=correio
    )
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
            private_chat=constants.PRIVATE_CHAT
        )
    )


@handler_bot
async def command_confesso_private_handler(
    Client: Client,
    message: Message,
    repository: Repository,
    utter_message: UtterMessage,
):
    if message.from_user and message.from_user.is_bot:
        return
    user_id = None
    user_name = None

    confissao = await message.chat.ask(
        utter_message["utter_boas_vindas_confesso"].text
    )
    if confissao.text.startswith("/"):
        await message.reply(utter_message["utter_cancelar_operacao"].text)
        return
    utter_fofoca = utter_message["utter_surpresa_confesso"]
    anonimo = await message.reply(
        utter_fofoca.text,
        reply_markup=utter_fofoca.keyboard,
    )
    response = await anonimo.wait_for_click()
    await response.message.edit_text(
        f"{response.message.text} = {response.data}"
    )
    if response.data == "/cancelar":
        await message.reply(utter_message["utter_cancelar_operacao"].text)
        return
    if response.data == "rejeitado":
        resposta = utter_message["utter_rejeitado_confesso"].text
    else:
        resposta = utter_message["utter_agradecendo_confesso"].text
        user_name = message.from_user.first_name
        user_id = message.from_user.id
    await message.reply(resposta)
    confesso = Confesso(
        mensagem=confissao.text, user_name=user_name, user_id=user_id
    )

    await usecases.confesso_usecase.create(
        repository=repository.confesso_repository, confesso_schema=confesso
    )


@handler_bot
async def command_feedback_handler_group(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_feedback_group"].text.format(
            private_chat=constants.PRIVATE_CHAT
        )
    )


@handler_bot
async def command_feedback_handler(
    Client: Client,
    message: Message,
    utter_message: UtterMessage,
    repository: Repository,
):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    utter_tipo_feedback = utter_message["utter_tipo_feedback"]
    feedback_message = await message.reply(
        utter_tipo_feedback.text.format(private_chat=constants.PRIVATE_CHAT),
        reply_markup=utter_tipo_feedback.keyboard,
    )
    tipo_feedback = await feedback_message.wait_for_click()

    feedback = await message.chat.ask(
        utter_message["utter_mensagem_feedback"].text
    )
    utter_entrar_em_contato_feedback = utter_message[
        "utter_entrar_em_contato_feedback"
    ]

    pode_contato_click = await message.reply(
        utter_entrar_em_contato_feedback.text,
        reply_markup=utter_entrar_em_contato_feedback.keyboard,
    )
    entrar_em_contato = await pode_contato_click.wait_for_click()
    entrar_em_contato = True if entrar_em_contato.data == "aceito" else False

    feedback = FeedBack(
        user_id=user_id,
        user_name=user_name,
        feedback=feedback.text,
        tipo_sugestao=tipo_feedback.data,
        pode_contato=entrar_em_contato,
    )
    await usecases.feedback_usecase.create(
        repository=repository.feedback_repository, feedback=feedback
    )
    await message.reply(utter_message["utter_agradecer_feedback"].text)


async def audio_voice_handler(Client: Client, message: Message):
    await message.reply("Opa! Começou o podcast! 🎙")
    await message.reply_voice(
        constants.UCRANIA_AUDIO_FILE,
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
        constants.ID_PHOTO_NAO_MANDA_FOTO,
        caption="Conhece aquela dupla sertaneja NemVi e NemVerei? 😂",
    )


@handler_bot
async def command_correio_group_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_correio_group"].text.format(
            private_chat=constants.PRIVATE_CHAT
        )
    )


@handler_bot
async def command_cerveja_handle(
    Client: Client,
    message: Message,
    repository: Repository,
    utter_message: UtterMessage,
):
    today = date.today()
    current_year = today.year
    data = await message.chat.ask(utter_message["utter_convite_cerveja"].text)
    try:
        day, month = data.text.split("/")
        agendado = date(year=current_year, month= int(month), day=int(day))
    except Exception as e:
        await message.reply(utter_message["utter_data_errada_cerveja"].text)
        await message.reply(utter_message["utter_repetir_comando_cerveja"].text)
        return
    
    faltam = agendado - today
    if faltam.days < 0:
        await message.reply(utter_message["utter_data_menor_que_hoje_cerveja"].text)
        await message.reply(utter_message["utter_repetir_comando_cerveja"].text)
        return
    elif faltam.days == 0:
        await message.reply(utter_message["utter_hoje_cerveja"].text)
    else:
        await message.reply(utter_message["utter_marcado_cerveja"].text.format(faltam=faltam.days))

    await message.reply(utter_message["utter_local_cerveja"].text)

    await Client.send_venue(
        message.chat.id,
        **constants.LOCATION_PARQUE_MADUREIRA,
        title="Parque Madureira",
        address="Rio de Janeiro",

    )
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    cerveja = Cerveja(user_id=user_id, user_name=user_name, data=data.text)
    await usecases.cerveja_usecase.create(
        repository=repository.cerveja_repository, cerveja_schema=cerveja
    )


@handler_bot
async def command_contact_handler(
    Client: Client, message: Message, utter_message: UtterMessage
):
    await message.reply(
        utter_message["utter_email_contato"].text.format(
            email_estacao=constants.ESTACAO_EMAIL
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )

    await message.reply(
        utter_message["utter_instagram_contato"].text.format(
            david_instagram=constants.DAVID_INSTAGRAM,
            rodrigo_instagram=constants.RODRIGO_INSTAGRAM,
            thauan_instagram=constants.THAUAN_INSTAGRAM,
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )


async def handle_callback_query(client, query: CallbackQuery):
    data = query.data
    await query.message.reply(data)


async def command_commands_handler(Client: Client, message: Message):
    comandos = await Client.get_bot_commands()
    bot_commands ="\n".join([f"Escreva /{comando.command} {comando.description}" for comando in comandos])
    await message.reply(bot_commands)
