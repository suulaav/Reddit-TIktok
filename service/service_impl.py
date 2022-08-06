from service.video.image_generator import generate_image
from service.reddit.reddit_service_impl import get_reddit_post
from service.tts.tts_generator import generate_mp3
from service.video.video_generator import generate_video


def start(subreddit):
    post = get_reddit_post(subreddit)
    text = post['title'] + " " + post['description']
    video_file_path = generate_video(generate_image(text), generate_mp3(text))
    return video_file_path
