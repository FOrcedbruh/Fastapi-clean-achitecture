from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from ..BaseRepository import BaseRepository
from schemas.users import UserUpdateSchema, UserReadSchema, UserReadWithPostsSchema
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .exceptions import UserNotFoundError, USER_NOT_FOUND_MESSAGE



class UserRepository(BaseRepository[User]):
    table = User
    exc = UserNotFoundError(messsage=USER_NOT_FOUND_MESSAGE, status_code=400)


    def __init__(self, session: AsyncSession):
        super().__init__(session=session, table=self.table, Exc=self.exc)


    async def update(self, id: int, data: UserUpdateSchema) -> UserReadSchema:
        res = await self.session.get(User, id)

        for name, val in data.model_dump(exclude_none=True).items():
            setattr(res, name, val)

        await self.session.commit()
        await self.session.refresh(res)

        return res


    async def get_with_posts(self, id: int) -> list[UserReadWithPostsSchema]:
        query = select(User).where(User.id == id).options(selectinload(User.posts))
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise self.exc

        return list(res)

