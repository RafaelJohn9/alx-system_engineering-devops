#!/usr/bin/python3
""" a module that containt the function "top_ten" function """

import requests


def top_ten(subreddit):
    """
    a function that queries the reddit api
    and prints the title of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user = {
            "User-Agent": "used to get the top ten posts in subreddit"
            }
    session = requests.get(url, headers=user)
    data = session.json()

    try:
        length = 0
        for value in data['data']['children']:
            if length == 10:
                break
            print(value['data']['title'])
            length += 1
    except Exception:
        print(None)
