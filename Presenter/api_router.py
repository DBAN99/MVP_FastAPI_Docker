from View import api_get,api_post,api_patch,api_delete
from fastapi import APIRouter

api_router = APIRouter

api_router.include_router(api_get.router, tags=["READ"])
api_router.include_router(api_post.router, tags=["CREATE"])
api_router.include_router(api_patch.router, tags=["UPDATE"])
api_router.include_router(api_delete.router, tags=["DELETE"])