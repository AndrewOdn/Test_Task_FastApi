from settings import USER_SEARCH_API_URL, API_HEADERS
import requests
from app.database.connections import twitter_base


def process_pipeline(self, usernames, meta):
    url = f"{USER_SEARCH_API_URL}?screen_name="
    for item in usernames:
        url += f"{item},"
        meta[item] = "PROGRESS"
    url = url[:-1]
    self.update_state(state='PROGRESS', meta=meta)
    data = get_response(url)
    insert_to_mongo(data)
    for item in usernames:
        meta[item] = "SUCCESS"
    self.update_state(state='PROGRESS', meta=meta)


def get_response(url):
    r = requests.get(url=url, headers=API_HEADERS)
    return r.json()


def insert_to_mongo(data):
    twitter_base["user_info"].insert_many(data)
