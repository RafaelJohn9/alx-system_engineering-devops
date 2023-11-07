#!/usr/bin/python3

""" 
this is a simple script that is used 
for checking the contents of the api stored in the file file.json
"""
import json
import requests

subreddit = "programming"
header = {
        "User-Agent": "Needs the total number of subscibers in a subreddit"
        }
url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
content = requests.get(url, headers=header)
print(content.json())
