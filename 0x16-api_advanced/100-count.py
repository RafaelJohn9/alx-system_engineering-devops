#!/usr/bin/python3
"""
a module that  sontaints the count_words fucntion
"""
import requests
import re


def count_words(subreddit, word_list, wordCount=None, after_token=None):
    if subreddit is None:
        return None

    if wordCount is None:
        wordCount = {}  # Initialize wordCount dictionary

    if after_token is None:
        after_token = ""  # Initialize after_token as an empty string

    # Base URL and User Agent
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Gets the trending data"}

    # Make an HTTP GET request to the Reddit API
    response = requests.get(
        base_url, params={"after": after_token},
        headers=headers
    )

    if response.status_code != 200:
        return None

    # Retrieve the 'after' token for pagination
    after_token = response.json().get("data").get("after")

    # Process each post in the response
    for post in response.json().get("data").get("children"):
        # Iterate through the list of words to count
        for word in word_list:
            # Use regex to find occurrences of the word in the post title
            pattern = re.escape(word.lower())
            target = post.get('data').get('title').lower()
            occur_count = len(re.findall(r'\b{}\b'.format(pattern), target))
            if occur_count > 0:
                # Update the word counts dictionary
                wordCount[word.lower()] = (
                        wordCount.get(word.lower(), 0) + occur_count)

    # If there are more posts to fetch, continue with the next page
    if after_token:
        return count_words(subreddit, word_list, wordCount, after_token)

    # If there are no more posts, print the word counts and return
    sorted_wordCount = sorted(wordCount.items(), key=lambda x: (-x[1], x[0]))
    for word, occurrence in sorted_wordCount:
        print('{}: {}'.format(word, occurrence))
    return wordCount
