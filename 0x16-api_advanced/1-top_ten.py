#!/usr/bin/python3
"""Module with a python script"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    ddlisted for a given subreddit
    """
    try:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {"User-Agent": "MyRedditBot"}
        response = requests.get(url, headers=headers)
        data = responses.json()
        for i in range(10):
            print(data["data"]["children"][i]["data"]["title"])
        return data["data"]
    except Exception:
        print("None")
