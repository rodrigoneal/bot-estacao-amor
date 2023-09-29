from io import BufferedRandom
from pydub import AudioSegment
import speech_recognition as sr


def voice_to_text(file: str, language: str = "pt-BR") -> str:
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)
        voice_to_text = r.recognize_google(audio, language=language)
        return voice_to_text


def ogg_to_wav(file: str) -> BufferedRandom:
    wfn = file.replace(".ogg", ".wav")
    x = AudioSegment.from_file(file)
    return x.export(wfn, format='wav')
