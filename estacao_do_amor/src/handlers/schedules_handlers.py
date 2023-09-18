import random
from pyrogram import Client
from pyrogram.types.user_and_chats.user import User
from pyrogram.types import ChatMember, Message

from estacao_do_amor.src.match.estacao_match import create_match
from estacao_do_amor.src.match.take_image import open_browser


estacao_id = -4014608746
async def generate_match(Client: Client, message: Message):
    # Pegada os membros do grupo
    members: list[ChatMember] = Client.get_chat_members(estacao_id)
    chat_info = await Client.get_chat(estacao_id)
    users = []
    # embaralhar a lista de membros
    members = [member async for member in members if not member.user.is_bot]
    random.shuffle(members)
    # Pega os dois primeiros membros e coloca em uma lista
    couple_members = members[0:2]
    
    for member in couple_members:
        user: User = member.user
        file_name = f"{user.id}.jpg"
        # Baixa a foto de perfil
        try:
            foto = await Client.download_media(user.photo.big_file_id, file_name=file_name)
        except AttributeError:
            foto = r"template.jpg"
        # Usando o objeto User para colocar a foto do usuário foda-se poo me permite fazer isso.
        user.foto = foto
        users.append(user)
    create_match(*users) # Criando o casal
    file_name = open_browser() # Baixando a imagem do tinder
    await Client.send_photo(
        chat_info.id, file_name, caption="Esse é o casal mais bonito desse grupo. "
    )