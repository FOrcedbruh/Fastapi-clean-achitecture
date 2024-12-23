from ..BaseRepository import BaseRepository
from models import Post
from sqlalchemy.ext.asyncio import AsyncSession



class PostRepository(BaseRepository[Post ]):
    table = Post
    tablename: str = "Пост"

    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, tablename=self.tablename)