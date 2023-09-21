from pyrogram import enums
from pyrogram.client import Client
from pyrogram.types import KeyboardButton, Message, ReplyKeyboardMarkup


async def progresso(
    current: int,
    total: int,
    Client: Client,
    chat_id: int,
    message_id: int,
):
    enviado = (current / total) * 100
    text = f"Enviado: {round(enviado, 2)}% Concluído."
    await Client.edit_message_text(chat_id,message_id, text)


async def create_youtube_video(Client: Client, message: Message):
    initial_message = await message.reply_text("Criando vídeo...")
    chat_id = initial_message.chat.id
    message_id = initial_message.id
    await message.reply_video(
        "/Users/rodrigoneal/Documents/projetos/bot-estacao-amor/video_final.mp4",
        progress=progresso,
        progress_args=(Client, chat_id, message_id),
    )
