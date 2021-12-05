from fastapi import APIRouter
from pydantic import BaseModel
from Model import db_class, db_conn
from Presenter import pre_request

router = APIRouter()
engine = db_conn.engineconn()
session = engine.sessionmaker()
connect = engine.connection()
task = db_class.Task

class Task_data(BaseModel):

    name: str
    completed: bool

@router.post("/task" , tags=["CREATE"])
async def post_task(data : Task_data):

    result = pre_request.pre_task_post(data)

    return result