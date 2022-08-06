import os

from flask import Flask, send_file
from service.service_impl import start

app = Flask(__name__)


@app.route("/make-video/<string:subreddit>")
def make_video(subreddit):
    return start(subreddit)


@app.route("/get-video")
def get_video():
    dir_path = "media/final/"
    res = os.listdir(dir_path)
    return send_file(dir_path + res[0], mimetype='video/mp4')


if __name__ == '__main__':
    app.run(debug=True)
