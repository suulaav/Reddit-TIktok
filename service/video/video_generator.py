import os
from datetime import datetime

from moviepy.editor import AudioFileClip, ImageClip


def generate_video(image_path, audio_path):
    dir = 'media/final'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    video_output_path = f"media/final/video_{datetime.now().strftime('%Y%m%d%H%M%S%z')}.mp4"
    video_clip.write_videofile(video_output_path)
    os.remove(image_path)
    os.remove(audio_path)
    return video_output_path
