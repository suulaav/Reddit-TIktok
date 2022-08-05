import logging
import random
import re

from service.reddit.config import reddit_login


def get_reddit_post(subreddit):
    reddit = reddit_login()
    title = []
    description = []
    for submission in reddit.subreddit(subreddit).new(limit=20):
        title.append(submission.title)
        description.append(submission.selftext)
    random_post_id = random.randint(1, 20)
    return {"title": title[random_post_id],
            "description": " ".join(re.split("\s+", description[random_post_id], flags=re.UNICODE))}
