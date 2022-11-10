from fastapi import APIRouter, Body
from ..process.users.tasks import get_add_task_user_info, get_users_data
from ..process.users.schemas import user_list_schema, task_schema
from starlette.responses import JSONResponse
router = APIRouter(tags=["users"])


@router.post("/users")
async def add_task_user(user_list: user_list_schema = Body(None)):
    task = get_users_data.apply_async(args=[[item[item.rfind('/') + 1:] for item in user_list.__root__]])
    return JSONResponse({"task_id": task.id})


@router.post("/users/status")
async def get_task_status(task_id: task_schema = Body(None)):
    return get_add_task_user_info(task_id.task_id)
