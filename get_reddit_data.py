import argparse
import praw

from credentials import CLIENT_ID
from credentials import CLIENT_SECRET
from credentials import USER_AGENT

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

comments_list = []
for submission in reddit.subreddit("mma").hot(limit=num_posts):
    # Ignore official posts as they are less "memey"
    if "[Official]" in submission.title:
        continue
    for comment in submission.comments:
        if comment is None or not hasattr(comment, "body"):
            continue
        comments_list.append(comment.body)

with open(filename, "w+") as reddit_file:
    for comment in comments_list:
        reddit_file.write("{}\n".format(comment))
