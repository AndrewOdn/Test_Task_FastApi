from fastapi import APIRouter
from app.process.user.database import get_user_info_from_db

router = APIRouter(tags=["user"])


@router.get("/user/{username}")
async def get_task_status(username: str):
    """
    Return the status of the submitted Task
    """
    return get_user_info_from_db(username)
