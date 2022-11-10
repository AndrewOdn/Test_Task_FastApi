from app.database.connections import twitter_base


def get_username_by_user_id(user_id):
    cursor = twitter_base['user_info'].find_one({"id": user_id})
    return cursor.get("screen_name")
