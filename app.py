import os

from flask import Flask, send_file
from service.service_impl import start

application = Flask(__name__)


@application.route("/make-video/<string:subreddit>")
def make_video(subreddit):
    return start(subreddit)


@application.route("/get-video")
def get_video():
    dir_path = "media/final/"
    res = os.listdir(dir_path)
    return send_file(dir_path + res[0], mimetype='video/mp4')


@application.route("/")
def ping():
    return "success"


if __name__ == '__main__':
    application.run(debug=True)
