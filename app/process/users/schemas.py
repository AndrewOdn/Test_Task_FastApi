from typing import List

from pydantic import BaseModel


class user_list_schema(BaseModel):
    __root__: List[str]


class task_schema(BaseModel):
    task_id: str
