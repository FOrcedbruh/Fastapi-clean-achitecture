from ..BaseRepository import BaseRepository
from models import Post
from sqlalchemy.ext.asyncio import AsyncSession
from .exceptions import PostNotFoundError, POST_NOT_FOUND_MESSAGE


class PostRepository(BaseRepository[Post ]):
    table = Post
    exc: PostNotFoundError = PostNotFoundError(messsage=POST_NOT_FOUND_MESSAGE, status_code=400)

    def __init__(self, session: AsyncSession):
        super().__init__(table=self.table, session=session, Exc=self.exc)