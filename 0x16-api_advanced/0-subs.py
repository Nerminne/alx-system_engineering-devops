#!/usr/bin/python3
"""Write a function that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns number of subscribers
        or 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':
               'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']

    return 0
