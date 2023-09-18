from moviepy.editor import VideoClip, AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from PIL import Image
import numpy as np

# Caminho para o arquivo de áudio
audio_path = 'estacao_do_amor/src/audio_video/musica.mp3'

# Caminho para a imagem
imagem_path = '/Users/rodrigoneal/Documents/projetos/bot-estacao-do-amor/estacao_do_amor/src/match/static/template.jpg'

# Função para criar um quadro com a imagem em movimento
def criar_quadro(t):
    # Carregue a imagem
    imagem = Image.open(imagem_path)    
    quadro = np.array(imagem)
    
    return quadro

# Crie um videoclipe com a imagem em movimento
video_clip = VideoClip(criar_quadro, duration=10)  # Defina a duração do vídeo (em segundos)

# Extraia o áudio do arquivo de áudio2
ffmpeg_extract_audio(audio_path, 'temp_audio.mp3')
# Carregue o áudio extraído
audio_clip = AudioFileClip('temp_audio.mp3')

# Combine o videoclipe com o áudio
video_final = video_clip.set_audio(audio_clip)

# Salve o vídeo final
video_final.write_videofile('video_final.mp4', codec='libx264', fps=24)

# Limpe os arquivos temporários
audio_clip.close()
video_clip.close()