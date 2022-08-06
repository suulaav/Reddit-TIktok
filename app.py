from service.video.image_generator import generate_image
from service.reddit.reddit_service_impl import get_reddit_post
from service.tts.tts_generator import generate_mp3
from textwrap3 import wrap

post = get_reddit_post("AmItheAsshole")

text = post['title'] + " " + post['description']
print(text)
generate_image(text)
generate_mp3(text)
