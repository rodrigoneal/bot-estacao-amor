import random
from tempfile import NamedTemporaryFile

from pyrogram import Client, enums
from pyrogram.types import ChatMember
from pyrogram.types.user_and_chats.user import User

from estacao_do_amor.src import constants
from estacao_do_amor.src.feed.feed_rss import AnchorFeed
from estacao_do_amor.src.match.estacao_match import create_match
from estacao_do_amor.src.match.take_image import download_image_match


async def generate_match(Client: Client):
    # Pegada os membros do grupo
    members: list[ChatMember] = Client.get_chat_members(constants.ESTACAO_ID)
    users = []
    # embaralhar a lista de membros
    members = [member async for member in members if not member.user.is_bot]
    random.shuffle(members)
    # Pega os dois primeiros membros e coloca em uma lista
    couple_members = members[0:2]
    with NamedTemporaryFile(suffix=".jpg", delete=False) as first_file, NamedTemporaryFile(suffix=".jpg", delete=False) as second_file:
        for member, file_name in zip(
            couple_members, (first_file, second_file)
        ):
            user: User = member.user
            # Baixa a foto de perfil
            try:
                foto = await Client.download_media(
                    user.photo.big_file_id, file_name=file_name.name
                )
            except AttributeError:
                foto = r"template.jpg"

            # Usando o objeto User para colocar a
            #  foto do usuário foda-se poo me permite fazer isso.
            user.foto = foto
            users.append(user)
        create_match(*users)  # Criando o casal
        with NamedTemporaryFile(suffix=".png", delete=False) as file:
            download_image_match(file.name)  # Baixando a imagem do tinder
            await Client.send_photo(
                constants.ESTACAO_ID,
                file.name,
                caption="Esse é o casal mais bonito desse grupo. ",
            )


async def last_episode(Client: Client):
    anchor_feed = AnchorFeed()
    last_episode = anchor_feed.podcast_episodes().episodes[0]
    await Client.send_message(
        constants.ESTACAO_ID,
        "Saiu mais um episodio do podcast mais apaixonante do mundo.",
        parse_mode=enums.ParseMode.MARKDOWN,
    )
    await Client.send_message(
        constants.ESTACAO_ID,
        "Episodio de hoje é: " + last_episode.title,
        parse_mode=enums.ParseMode.HTML,
    )
    await Client.send_message(
        constants.ESTACAO_ID,
        last_episode.summary,
        parse_mode=enums.ParseMode.HTML,
    )
    await Client.send_message(
        constants.ESTACAO_ID,
        (
            "Entre agora nesse link "
            "e ouça os mais amados - "
            f"[Estação do amor]({constants.URL_SPOTIFY})"
        ),
        parse_mode=enums.ParseMode.MARKDOWN,
    )
