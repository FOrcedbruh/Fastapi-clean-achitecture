from fastapi import APIRouter
from .users import router as UsersRouter
from .posts import router as PostsRouter

router = APIRouter(prefix="/api")
router.include_router(router=UsersRouter)
router.include_router(router=PostsRouter)