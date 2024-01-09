from datetime import datetime, timezone
from sqlalchemy import BigInteger, String, ForeignKey, text
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from typing import Annotated

intpk = Annotated[int, mapped_column(BigInteger, primary_key=True, autoincrement=True, sort_order=-1)]
created_at_type = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at_type = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                    onupdate=datetime.now(timezone.utc))]
str_255_unique = Annotated[str, mapped_column(String(255), nullable=False, unique=True)]
str_255_not_null = Annotated[str, mapped_column(String(255), nullable=False)]


class Base(DeclarativeBase):
    id: Mapped[intpk]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[updated_at_type]


class User(Base):
    __tablename__ = 'users'
    login: Mapped[str_255_unique]
    password: Mapped[str] = mapped_column(nullable=False)


class Item(Base):
    __tablename__ = 'items'
    name: Mapped[str_255_not_null]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
