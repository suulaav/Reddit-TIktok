from gtts import gTTS
from datetime import datetime


def generate_mp3(text):
    tts = gTTS(text)
    file_path = f'media/temp/speech_{datetime.now().strftime("%Y%m%d%H%M%S%z")}.mp3'
    tts.save(file_path)
    return file_path
