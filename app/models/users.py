from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .posts import Post


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(10), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    isHappy: Mapped[bool] = mapped_column(nullable=False)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
