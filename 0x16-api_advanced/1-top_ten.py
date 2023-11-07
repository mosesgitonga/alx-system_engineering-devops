#!/usr/bin/python3
"""
find top 10 hot posts
"""
import requests

def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {"user-agent": "O1UydnAcwk03Z2sAuoef8g"}
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)

    response = requests.get(url, headers=user_agent)
   
    res = response.json()
    try:
        res = res.get('data')
        children = res.get('children')
        for post in children:
            print(post.get('data').get('title'))

    except Exception:
        print('None')
    