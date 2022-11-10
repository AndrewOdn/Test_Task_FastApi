from app.database.connections import twitter_base


def get_user_info_from_db(username):
    cursor = twitter_base['user_info'].find_one({"screen_name": username})
    return {
        "twitter_id": cursor.get("id"),
        "name": cursor.get("name"),
        "username": cursor.get("screen_name"),
        "following": cursor.get("friends_count"),
        "followers": cursor.get("followers_count"),
        "description": cursor.get("description")
    }
