#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
import requests
from requests import get
import sys


def number_of_subscribers(subreddit):
    """
    find num of suscribers
    """
    if subreddit is None or not isinstance(subreddit, str):
       
        return 0

    user_agent = {"user-agent": "O1UydnAcwk03Z2sAuoef8g"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=user_agent)
    res = response.json()
    try:
        return res.get('data').get('subscribers')
    except Exception:
        return 0
