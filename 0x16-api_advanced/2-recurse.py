#!/usr/bin/python3
"""Module with a python script"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Method that uses recursive method to get top 10 hot titles"""
    global after
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(
            url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        nextO = response.json().get('data').get('after')
        if nextO is not None:
            after = next_obj
            recurse(subreddit, hot_list)
        listT = response.json().get('data').get('children')
        for oTitle in listT:
            hotList.append(oTitle.get('data').get('title'))
        return hotList
    else:
        return None
