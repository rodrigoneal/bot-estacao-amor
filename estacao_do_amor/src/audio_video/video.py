import numpy as np
from moviepy.editor import AudioFileClip, VideoClip
from PIL import Image


def create_video(image_path: str, audio_path: str, filename: str):
    def criar_quadro(t):
        # Carregue a imagem
        imagem = Image.open(image_path)
        imagem.resize((1298, 720))
        quadro = np.array(imagem)

        return quadro

    # Crie um videoclipe com a imagem em movimento
    video_clip = VideoClip(criar_quadro, duration=10)

    audio_clip = AudioFileClip(audio_path)
    video_final = video_clip.set_audio(audio_clip)
    video_final.write_videofile(filename, codec="libx264", fps=24, threads=6)
    audio_clip.close()
    video_clip.close()
