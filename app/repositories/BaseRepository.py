from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base
from sqlalchemy import select
from .exceptions import NotFoundError




TableType = TypeVar(name="TableType", bound=Base)


class BaseRepository(Generic[TableType]):
    def __init__(self, table: TableType, session: AsyncSession, tablename: str):
        self.table = table
        self.session = session
        self.tablename = tablename


    async def list(self) -> list[TableType]:
        query = select(self.table)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise NotFoundError(messsage=f"{self.tablename} не найдены", status_code=400)
        return list(res)
    
    async def get(self, id: int) -> TableType:
        res = await self.session.get(self.table, id)
        if not res:
            raise NotFoundError(messsage=f"{self.tablename} не найден", status_code=400)
        return res
    
    async def create(self, data: TableType) -> TableType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)
        return data

    
    async def delete(self, id: int) -> None:
        res = await self.session.get(self.table, id)

        if not res:
            raise NotFoundError(messsage=f"{self.tablename} не найден", status_code=400)
        await self.session.delete(res)
        await self.session.commit()


