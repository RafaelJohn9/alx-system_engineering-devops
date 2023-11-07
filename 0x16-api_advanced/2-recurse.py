#!/usr/bin/python3
"""
a module that contains:
a function that queries the Reddit API
and returns a list containing the titles of trending titles
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    function that utilizes recursion for it
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    children = data.get('children')
    after = data.get('after')

    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after)

    return hot_list
