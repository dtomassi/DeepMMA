import argparse
import json
import praw

from credentials import CLIENT_ID, CLIENT_SECRET, USER_AGENT

parser = argparse.ArgumentParser()
parser.add_argument(
    "-o", metavar="filename", type=str, nargs=1, help="filename for output file."
)
parser.add_argument(
    "-n",
    metavar="num_posts",
    type=int,
    nargs=1,
    help="Number of posts to gather comments from.",
)

args = parser.parse_args()
filename = args.o[0]
num_posts = args.n[0]

reddit = praw.Reddit(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT
)

count = 0
comments_dict = {}
for submission in reddit.subreddit("mma").hot(limit=num_posts):
    # Ignore official posts as they are less "memey"
    if "[Official]" in submission.title:
        continue
    for comment in submission.comments:
        if comment is None or not hasattr(comment, "body"):
            continue
        comments_dict[count] = comment.body.strip()
        count += 1

with open(filename, "w+") as reddit_file:
    json.dump(comments_dict, reddit_file, indent=4)
