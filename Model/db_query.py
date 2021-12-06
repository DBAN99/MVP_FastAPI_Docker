from Model import db_conn
from Model import db_class

engine = db_conn.engineconn()
session = engine.sessionmaker()
task = db_class.Task

# session commit 부분
def db_commit():

    return session.commit()

# session close 부분
def db_close():

    return session.close()

# GET /task 부분
def db_task_get_all():

    result = session.query(task).all()

    return result

# GET /task/{id} 부분
def db_task_get_id(id):

    result = session.query(task).filter(task.id == id).all()

    return result

# POST /task  부분
def db_task_post(data):

    addMemo = task(name=data.name, completed=data.completed)
    result = session.add(addMemo)
    return result

# PATCH /task/{id} 부분
def db_task_patch(id, edit):
    result = session.query(task).filter(task.id == id).update({'completed':edit.completed})

    return result

# DELETE /task
def db_task_delete_all():
    result = session.query(task).delete()
    return result

# DELETE /task/{id}
def db_task_delete_id(id):
    result = session.query(task).filter(task.id == id).delete()

    return result