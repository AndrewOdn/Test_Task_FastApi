from fastapi import APIRouter, Body, Depends, Query
from ..process.tweets.worker import get_last_tweets_by_user_id
router = APIRouter(tags=["tweets"])


@router.get("/tweets/{twitter_id}")
async def get_tweets(twitter_id: int):
    return get_last_tweets_by_user_id(twitter_id)
