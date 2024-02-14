#!/usr/bin/python3
"""Module with a python script"""
import requests
after = None
countD = []


def count_words(subreddit, word_list):
    """queries Reddit api"""
    global after
    global countD
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, headers=headers, allow_redirects=False, params=params)
