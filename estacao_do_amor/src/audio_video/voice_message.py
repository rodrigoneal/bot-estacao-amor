from io import BufferedRandom
from tempfile import NamedTemporaryFile
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr
from pyrogram.client import Client
from pyrogram.types import Message



def _voice_to_text(file: str, language: str = "pt-BR") -> str:
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        voice_to_text = r.recognize_google(audio, language=language)
        return voice_to_text


def ogg_to_wav(file: str) -> BufferedRandom:
    wfn = file.replace(".ogg", ".wav")
    x = AudioSegment.from_file(file)
    return x.export(wfn, format='wav')

async def voice_to_text(Client: Client, mensagem: Message) -> str:
    with NamedTemporaryFile(suffix=".ogg", delete=False) as f:
        file_name = f.name
        await Client.download_media(message=mensagem, file_name=file_name)
        wav_file = ogg_to_wav(file_name)
        mensagem = _voice_to_text(wav_file)
        return mensagem

def text_to_voice(text: str, file_name: str) -> str:
    tts = gTTS(text, lang='pt-br') 
    tts.save(file_name)