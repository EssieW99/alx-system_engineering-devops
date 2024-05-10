#!/usr/bin/python3
""" query to the Reddit API"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """

    limit = 10
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit={limit}"
    headers = {'User-Agent': 'MyAPI/7.68.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        for post in hot_posts:
            print(post['data']['title'])
    else:
        print(None)
