from pyrogram.client import Client
from pyrogram.types import Message

from estacao_do_amor.src import CONSTANTS


async def audio_voice_exception(Client: Client, message: Message):
    await Client.send_audio(
        message.chat.id,
        CONSTANTS.ID_AUDIO_UCRANIA,
        duration=6,
        caption=(
            "Não mande áudios que"
            " eu não sou nenhuma safada pra ficar ouvindo áudios"
        ),
    )


async def imagem_video_exception(Client: Client, message: Message):
    await Client.send_audio(
        message.chat.id,
        CONSTANTS.ID_PHOTO_NAO_MANDA_FOTO,
        duration=6,
        caption="A dupla sertaneja NemVi e NemVerei. 😂",
    )
