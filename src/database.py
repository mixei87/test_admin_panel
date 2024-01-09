from config import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(url=settings.db_url)
session_factory = async_sessionmaker(engine)
