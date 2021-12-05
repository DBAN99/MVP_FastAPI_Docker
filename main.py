from View import api_get,api_delete,api_post,api_patch
from fastapi import FastAPI
from Model import db_install

def include_router(app):
    app.include_router(api_get.router)
    app.include_router(api_delete.router)
    app.include_router(api_post.router)
    app.include_router(api_patch.router)

def start_application():
    app = FastAPI()
    include_router(app)
    return app

db_install.table_install()

app = start_application()
