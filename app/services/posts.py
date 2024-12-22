from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from config import db
from repositories import PostRepository
from schemas.posts import PostReadSchema, PostCreateSchema
from models import Post

class PostService:
    def __init__(self, session: AsyncSession = Depends(db.generate_session)):
        self.repository = PostRepository(session=session)

    async def get_posts(self) -> list[PostReadSchema]:
        return await self.repository.list()
    
    async def get_post(self, post_id: int) -> PostReadSchema:
        return await self.repository.get(id=post_id)
    
    async def delete_post(self, post_id: int) -> dict:
        await self.repository.delete(id=post_id)

        return {
            "message": "Пост успешно удален"
        }
    
    async def create_post(self, post_in: PostCreateSchema) -> PostReadSchema:
        post_for_create = Post(**post_in.model_dump())
        return await self.repository.create(data=post_for_create)
