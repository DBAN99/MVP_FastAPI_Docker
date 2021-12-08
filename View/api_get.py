from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

@router.get("/task" , tags=["READ"])
async def get_task():
    result = pre_request.pre_task_get_all()

    return result

@router.get("/task/{id}" , tags=["READ"])
async def get_task_id(id : int):
    result = pre_request.pre_task_get_id(id)

    return result




