from pydantic import BaseModel
from datetime import datetime
from .posts import PostReadSchema


class UserCreateSchema(BaseModel):
    username: str
    age: int
    isHappy: bool

class UserReadSchema(UserCreateSchema):
    id: int
    created_at: datetime

class UserUpdateSchema(BaseModel):
    username: str | None = None
    age: int | None = None
    isHappy: bool | None = None

class UserReadWithPostsSchema(UserReadSchema):
    posts: list[PostReadSchema]