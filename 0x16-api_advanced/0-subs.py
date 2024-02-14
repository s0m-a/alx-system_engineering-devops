#!/usr/bin/python3
"""Module with python script"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries  and returns the number of
    subscribers for a given subreddit.
    """
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
