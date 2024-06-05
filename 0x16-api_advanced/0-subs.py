#!/usr/bin/python3
"""Write a function that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
        Return num of subscribers
        or zero if invalid subreddit is given
    """
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}
    url = 'https://api.reddit.com/r/{}/about/'.format(subreddit)
    res = requests.get(url,  headers=u_agent)
    if res.status_code == 200:
        subs = res.json()["data"]["subscribers"]
    else:
        subs = 0
    return subs
