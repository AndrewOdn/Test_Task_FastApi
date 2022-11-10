from app.routers import users, user, tweets
from app.celery.celery_utils import create_celery
from fastapi import FastAPI
import uvicorn
api_title = "twitter-management-api"
api_version = "0.0.1"
api_description = "twitter-management-api"

app = FastAPI(title=api_title, version=api_version, description=api_description)
app.celery_app = create_celery()
app.include_router(users.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(tweets.router, prefix="/api")
celery = app.celery_app
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
