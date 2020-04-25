import flask
import praw 
from praw.models import MoreComments
from praw.models import Submission
import requests
import json
import numpy as np
import pandas as pd

client_id = 'gLwv0aerGRmt9A'
client_secret = 'hYQwRYZJVEUgKzJ7jrLIx8RT7ZE'
user_agent = 'Midas'

reddit = praw.Reddit(client_id= client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)



def submission(url):
    data = {}
    submission  = Submission(reddit = reddit, url = url)
    data['author'] = submission.author
    data['content'] = submission.selftext
    data['flair'] = submission.link_flair_text
    data['subreddit'] = submission.subreddit
    data['title'] = submission.title
    return data
