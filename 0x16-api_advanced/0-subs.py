#!/usr/bin/python3
"""Module with python script"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries  and returns the number of
    subscribers for a given subreddit.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
