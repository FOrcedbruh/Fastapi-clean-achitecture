from pydantic import BaseModel
from datetime import datetime


class PostCreateSchema(BaseModel):
    title: str
    body: str
    user_id: int


class PostReadSchema(PostCreateSchema):
    id: int
    created_at: datetime

class PostUpdateSchema(BaseModel):
    title: str | None = None
    body: str | None = None