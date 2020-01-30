from fastapi import APIRouter

from . import resource1, resource2

router = APIRouter()
router.include_router(resource1.router, tags=['resource1'], prefix='/resource1')
router.include_router(resource2.router, tags=['resource2'], prefix='/resource2')
