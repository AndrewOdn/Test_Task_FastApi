import requests
from settings import TWEET_SEARCH_API_URL, API_HEADERS
from .database import get_username_by_user_id


def get_last_tweets_by_user_id(user_id, count=10):
    username = get_username_by_user_id(user_id)
    response = requests.get(url=f"{TWEET_SEARCH_API_URL}?q=from:{username}&count={count}", headers=API_HEADERS)
    tweets = response.json()
    return [item.get("text") for item in tweets['statuses']]
