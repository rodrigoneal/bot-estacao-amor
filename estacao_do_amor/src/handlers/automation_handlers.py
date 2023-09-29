import tempfile
from io import BytesIO

from pyrogram.client import Client
from pyrogram.types import Message

# from estacao_do_amor.src.audio_video.video import create_video


async def progress_media(
    current: int, total: int, Client: Client, message: Message, media_type: str
):
    enviado = (current / total) * 100
    text = f"{media_type}: {round(enviado, 2)}% Concluído."
    await Client.edit_message_text(message.chat.id, message.id, text)


async def create_youtube_video(Client: Client, message: Message):
    # Pedindo as midias para criar o video.
    with tempfile.NamedTemporaryFile(
        suffix=".jpg"
    ) as imagem_file, tempfile.NamedTemporaryFile(
        suffix=".mp3"
    ) as audio_file, tempfile.NamedTemporaryFile(
        suffix=".mp4"
    ) as video_file:
        # Salvando imagem
        ep_image: Message = await message.chat.ask(
            "Me envie a thumbnail do episodio. 🖼"
        )
        write_progress = await message.reply_text(
            "Salvando imagem, aguarde..."
        )
        temporary_image: BytesIO = await ep_image.download(
            in_memory=True,
            progress=progress_media,
            progress_args=(Client, write_progress, "Salvando imagem"),
        )
        # Salvando audio
        ep_audio: Message = await message.chat.ask(
            "Me envie o audio do episodio. 🎙"
        )
        write_progress = await message.reply_text("Salvando audio, aguarde...")
        temporary_audio: BytesIO = await ep_audio.download(
            in_memory=True,
            progress=progress_media,
            progress_args=(Client, write_progress, "Salvando audio"),
        )

        # Gravando no arquivo tempório
        imagem_file.write(temporary_image.getvalue())
        audio_file.write(temporary_audio.getvalue())
        # Criando o video
        await message.reply_text(
            "Criando o video, pode demorar alguns segundos..."
        )
        create_video(imagem_file.name, audio_file.name, video_file.name)
        # Uploadando o video
        upload_messsage = await message.reply_text("Criando vídeo...")
        await message.reply_video(
            video_file.name,
            progress=progress_media,
            progress_args=(Client, upload_messsage, "Enviando Video"),
        )
    temporary_image.close()
    temporary_audio.close()
