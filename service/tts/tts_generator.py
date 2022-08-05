from gtts import gTTS
from datetime import datetime


def generate_mp3(text):
    tts = gTTS(text["data"])
    file_path = f'mp3s/speech_{datetime.now().strftime("%Y%m%d%H%M%S%z")}.mp3'
    tts.save(file_path)
    return file_path
