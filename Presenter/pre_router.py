from View import api_get,api_post,api_patch,api_delete
from fastapi import APIRouter

router = APIRouter

router.include_router(api_get.router, tags=["READ"])
router.include_router(api_post.router, tags=["CREATE"])
router.include_router(api_patch.router, tags=["UPDATE"])
router.include_router(api_delete.router, tags=["DELETE"])