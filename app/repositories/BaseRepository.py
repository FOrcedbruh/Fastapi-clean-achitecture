from typing import Generic, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base
from sqlalchemy import select
from .exceptions import NotFoundError




TableType = TypeVar(name="TableType", bound=Base)
ExcType = TypeVar(name="ExcType", bound=NotFoundError)


class BaseRepository(Generic[TableType]):
    def __init__(self, table: TableType, session: AsyncSession, Exc: ExcType):
        self.table = table
        self.session = session
        self.Exc = Exc


    async def list(self) -> list[TableType]:
        query = select(self.table)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise self.Exc
        return list(res)
    
    async def get(self, id: int) -> TableType:
        res = await self.session.get(self.table, id)
        if not res:
            raise self.Exc
        return res
    
    async def create(self, data: TableType) -> TableType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)
        return data

    
    async def delete(self, id: int) -> None:
        res = await self.session.get(self.table, id)

        if not res:
            raise self.Exc
        await self.session.delete(res)
        await self.session.commit()


