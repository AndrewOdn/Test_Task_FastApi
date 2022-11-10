import pymongo
from settings import mongo_url
mongo_client = pymongo.MongoClient(mongo_url)
twitter_base = mongo_client["Twitter"]