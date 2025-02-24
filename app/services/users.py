from repositories import UserRepository
from schemas.users import UserCreateSchema, UserUpdateSchema, UserReadSchema, UserReadWithPostsSchema
from models import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from config import DB

local_session = DB()

class UserService:
    def __init__(self, session: AsyncSession = Depends(local_session.generate_session)) -> None:
        self.repository = UserRepository(session=session)


    async def get_users(self) -> list[UserReadSchema]:
        return await self.repository.list()

    async def get_user(self, user_id: int) -> UserReadSchema:
        return await self.repository.get(id=user_id)
    

    async def create_user(self, user_in: UserCreateSchema) -> UserReadSchema:
        user_for_create = User(**user_in.model_dump())
        new_user = await self.repository.create(data=user_for_create)

        return new_user

    async def update_user(self, user_in: UserUpdateSchema, user_id: int) -> UserReadSchema:
        updated_user = await self.repository.update(data=user_in, id=user_id)

        return updated_user
    
    async def delete_user(self, user_id: int) -> dict:
        await self.repository.delete(id=user_id)

        return {
            "message": "Пользователь успешно удален"
        }
    
    async def get_user_with_posts(self, user_id: int) -> list[UserReadWithPostsSchema]:
        return await self.repository.get_with_posts(id=user_id)
