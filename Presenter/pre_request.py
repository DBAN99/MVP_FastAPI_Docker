from fastapi.responses import JSONResponse
from Model import db_query
from Model import db_conn

engine = db_conn.engineconn()
session = engine.sessionmaker()
commit = db_query.db_commit
close = db_query.db_close

# ---------------------- GET ----------------------

def pre_task_get_all():

    try:
        result = db_query.db_task_get_all()

    except:
        result = JSONResponse(status_code=400, content={"message":" 400 Validation Failure"})

    else:
        if result == []:

            result = JSONResponse(status_code=404,content={"message":"404 Data Not Found "})
    finally:
        close()
    return result

def pre_task_get_id(id):
    try:
        result = db_query.db_task_get_id(id)

    except:
        result = JSONResponse(status_code=400, content={"message":" 400 Bad Request"})

    else:
        if result == []:
            result = JSONResponse(status_code=404,content={"message":"404 Data Not Found "})
    finally:
        close()

    return result

# ---------------------- POST ----------------------

def pre_task_post(data):

    if data.name == "" or type(data.completed) != bool:
        result = JSONResponse(status_code=400, content={"message": "400 Bad Request "})

    else:

        try:
            db_query.db_task_post(data)
            commit()
        except:
            result = JSONResponse(status_code=400, content={"message": "400 Bad Request"})

        else:
            result = JSONResponse(status_code=200, content={"message": "200 OK"})

        finally:
            close()

    return result

# ---------------------- DELETE ----------------------

def pre_task_delete_all():
    del_result =db_query.db_task_delete_all()

    if del_result == 0:
        result = JSONResponse(status_code=404, content={"message": "404 Data Not Found"})

    else:
        try:
            commit()

        except:
            result = JSONResponse(status_code=400, content={"message": "400 Bad Request"})

        else:
            result = JSONResponse(status_code=200, content={"message": " 200 OK"})

        finally:
            close()

    return result

def pre_task_delete_id(id):
    del_result = db_query.db_task_delete_id(id)

    if del_result == 0:
        result = JSONResponse(status_code=404, content={"message":"404 Data Not Found"})

    else:

        try:
            commit()

        except:
            result = JSONResponse(status_code=400, content={"message":"400 Bad Request"})

        else:
            result = JSONResponse(status_code=200, content={"message":" 200 OK"})

        finally:
            close()

    return result

# ---------------------- PATCH ----------------------

def pre_task_patch(id,edit):

    patch_result = db_query.db_task_patch(id,edit)

    if patch_result == 0:
        result = JSONResponse(status_code=404, content={"message": "404 Data Not Found"})

    else:

        try:
            commit()

        except:
            result = JSONResponse(status_code=400, content={"message": "400 Bad Request"})

        else:
            result = JSONResponse(status_code=200, content={"message": " 200 OK"})

        finally:
            close()

    return result