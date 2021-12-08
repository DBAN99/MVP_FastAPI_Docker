from fastapi import APIRouter
from pydantic import BaseModel
from Presenter import pre_request

router = APIRouter()

class Task_data(BaseModel):
    name: str
    completed: bool

@router.post("/task" , tags=["CREATE"])
async def post_task(data : Task_data):
    result = pre_request.pre_task_post(data)

    return result