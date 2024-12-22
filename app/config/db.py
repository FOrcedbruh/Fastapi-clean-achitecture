from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from .settings import settings
from typing import AsyncGenerator


class DB():
    def __init__(self, db_url: str = settings.db.url, echo: bool = settings.db.echo):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo
        )
        self.session_factory: AsyncGenerator[AsyncSession, None] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def generate_session(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session



db = DB()