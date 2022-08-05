import datetime

from service.reddit.reddit_service_impl import get_reddit_post
from service.tts.tts_generator import generate_mp3

result = get_reddit_post("AmItheAsshole")
data = result["title"] + "\n" + result["description"]
print(data)
file_path = generate_mp3({"data": data})
print(file_path)

