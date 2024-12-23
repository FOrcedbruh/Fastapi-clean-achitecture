from sqlalchemy.ext.asyncio import AsyncSession
from models import User
from ..BaseRepository import BaseRepository
from schemas.users import UserUpdateSchema, UserReadSchema
from sqlalchemy import select
from sqlalchemy.orm import selectinload



class UserRepository(BaseRepository[User]):
    table = User
    tablename: str = "Пользователь"
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, table=self.table, tablename=self.tablename)

    async def update(self, id: int, data: UserUpdateSchema) -> UserReadSchema:
        res = await self.session.get(User, id)

        for name, val in data.model_dump(exclude_none=True).items():
            setattr(res, name, val)

        await self.session.commit()
        await self.session.refresh(res)

        return res

    async def get_with_posts(self, id: int):
        query = select(User).where(User.id == id).options(selectinload(User.posts))
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()


        return list(res)

