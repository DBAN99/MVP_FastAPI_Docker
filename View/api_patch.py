from fastapi import APIRouter
from pydantic import BaseModel

from Presenter import pre_request

router = APIRouter()

class Task_edit(BaseModel):
    completed : bool

@router.patch("/task/{id}" , tags=["UPDATE"])
async def patch_task_id(id : int, edit : Task_edit):
    result = pre_request.pre_task_patch(id,edit)

    return result