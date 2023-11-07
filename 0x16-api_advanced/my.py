#!/usr/bin/python3

""" 
this is a simple script that is used 
for checking the contents of the api stored in the file file.json
"""
import json
import requests

subreddit = "programming"
url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

user = {
        "User-Agent": "used to get the top ten posts in subreddit"
        }
session = requests.get(url, headers=user)
data = session.json()

len = 0
try:
    for value in data['data']['children']:
        print(value)
        if len == 10:
            break
        len += 1
except Exception:
    print(data)
