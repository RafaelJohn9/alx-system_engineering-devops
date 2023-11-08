#!/usr/bin/python3
"""
a module that  sontaints the count_words fucntion
"""
import re
import requests


def count_words(subreddit, words_to_count, wordCount={}, after_token=""):
    """
    Count the occurrences of words in the titles of hot posts in a subreddit.
    """
    if subreddit is None:
        return None

    # Construct the URL for Reddit's hot posts in the specified subreddit
    base_url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Define a user agent to make the API request
    headers = {"User-Agent": "Gets the trending data"}

    # Make an HTTP GET request to the Reddit API
    response = requests.get(
                           base_url, params={"after": after_token},
                           headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Retrieve the 'after' token for pagination
        after_token = response.json().get("data").get("after")

        # If there are no more posts to fetch, print the word counts and exit
        if not after_token:
            sorted_wordCount = sorted(wordCount.items(),
                                      key=lambda x: (-x[1], x[0]))

            for word, occurrence in sorted_wordCount:
                print('{}: {}'.format(word, occurrence))
            return

        # Process each post in the response
        for post in response.json().get("data").get("children"):
            # Iterate through the list of words to count
            for word in words_to_count:
                # Use regex to find occurrences of the word in the post title
                pattern = re.escape(word.lower())
                target = post.get('data').get('title').lower()
                occur_count = len(re.findall(r'\b{}\b'.
                                  format(pattern), target))
                if occur_count > 0:
                    # Update the word counts dictionary
                    wordCount[word.lower()] = (
                            wordCount.get(word, 0) + occur_count
                            )

        # Continue to the next page of posts
        return count_words(subreddit, words_to_count, wordCount, after_token)
