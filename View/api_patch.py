from fastapi import APIRouter
from pydantic import BaseModel
from Model import db_class, db_conn
from Presenter import pre_request

router = APIRouter()
engine = db_conn.engineconn()
session = engine.sessionmaker()
connect = engine.connection()
task = db_class.Task

class Task_edit(BaseModel):

    completed : bool

@router.patch("/task/{id}" , tags=["UPDATE"])
async def patch_task_id(id : int, edit : Task_edit):

    result = pre_request.pre_task_patch(id,edit)

    return result