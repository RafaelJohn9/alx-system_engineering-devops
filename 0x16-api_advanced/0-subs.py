#!/usr/bin/python3

"""
a script that fetches amount of subreditts in a particular search query
"""

def number_of_subscribers(subreddit):
    import requests

    url = "https://www.reddit.com/subreddits/search.json?q={}".format(subreddit)
    headers = {
            'User-Agent': 'MyRedditApp/1.0'
            }

    session = requests.get(url, headers)
    if (session.status_code == 200):
       return (len(session.json()['data']))
    else:
        return (0);
