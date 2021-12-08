from fastapi import APIRouter
from Presenter import pre_request

router = APIRouter()

@router.delete("/task" , tags=["DELETE"])
async def delete_task():
    result = pre_request.pre_task_delete_all()

    return result

@router.delete("/task/{id}" , tags=["DELETE"])
async def delete_task_id(id: int):
    result = pre_request.pre_task_delete_id(id)

    return result