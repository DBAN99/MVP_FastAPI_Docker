from fastapi import APIRouter
from pydantic import BaseModel
from Model import db_class, db_conn
from Presenter import pre_request

router = APIRouter()
engine = db_conn.engineconn()
session = engine.sessionmaker()
connect = engine.connection()
task = db_class.Task

@router.delete("/task" , tags=["DELETE"])
async def delete_task():

    result = pre_request.pre_task_delete_all()

    return result

@router.delete("/task/{id}" , tags=["DELETE"])
async def delete_task_id(id: int):

    result = pre_request.pre_task_delete_id(id)

    return result