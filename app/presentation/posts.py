from fastapi import APIRouter, Depends, Body
from schemas.posts import PostReadSchema, PostCreateSchema
from services.posts import PostService


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[PostReadSchema])
async def index(
    service: PostService = Depends(PostService)
) -> list[PostReadSchema]:
    return await service.get_posts()


@router.get("/{post_id}", response_model=PostReadSchema)
async def index(
    post_id: int,
    service: PostService = Depends(PostService)
) -> PostReadSchema:
    return await service.get_post(post_id=post_id)


@router.post("/create", response_model=PostReadSchema)
async def index(
    service: PostService = Depends(PostService),
    post_in: PostCreateSchema = Body()
) -> PostReadSchema:
    return await service.create_post(post_in=post_in)


@router.delete("/delete/{post_id}")
async def index(
    post_id: int,
    service: PostService = Depends(PostService)
):
    return await service.delete_post(post_id=post_id)


