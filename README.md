# DeepMMA
Inspired by https://twitter.com/deepleffen

We aim to train a model based on 1558M version of OpenAI's GPT-2 model from https://www.reddit.com/r/MMA/ comments. With the goal to create interesting and humorous text.

## Installation
```$ pip3 install -r requirements.txt```

## Credentials for Reddit API
Fill in the missing information from `credentials.sample.py`
```
CLIENT_ID = "ID"
CLIENT_SECRET = "SECRET"
USER_AGENT = "APP"
```
into a new file called `credentials.py`

## Retrieving Reddit comments
```$ python3 get_reddit_data.py -o <output-filename> -n <number-of-posts-to-get>```
