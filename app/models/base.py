from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
import datetime


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now())