#!/usr/bin/python3
"""Python script module for retrieving top titles from a subreddit."""

import requests

after = None


def get_top_titles(subreddit, title_list=[]):
    """Recursively fetches top titles from the specified subreddit."""
    global after
    headers = {'User-Agent': 'Reddit API'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)
    
    if response.status_code == 200:
        next_page = response.json().get('data').get('after')
        
        if next_page is not None:
            after = next_page
            get_top_titles(subreddit, title_list)
        
        titles = response.json().get('data').get('children')
        for title in titles:
            title_list.append(title.get('data').get('title'))
        
        return title_list
    
    else:
        return None
