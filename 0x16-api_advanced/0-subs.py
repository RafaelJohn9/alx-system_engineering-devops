#!/usr/bin/python3
""" module of the function number_of_subscribers """

import requests


def number_of_subscribers(subreddit):
    """
    counts the number or subscribers in a subreddit
    """
    header = {
            "User-Agent": "Needs the total number of subscibers in a subreddit"
            }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    content = requests.get(url, header)
    data = content.json()

    return (data.get("data", {}).get("subscribers", 0))
