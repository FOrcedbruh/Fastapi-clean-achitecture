from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from .base import Base
from .users import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String(30), nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="posts")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
