from gtts import gTTS
from datetime import datetime


def generate_mp3(text):
    tts = gTTS(text)
    audio_path = f'media/temp/speech_{datetime.now().strftime("%Y%m%d%H%M%S%z")}.mp3'
    tts.save(audio_path)
    return audio_path
