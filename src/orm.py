from database import engine, session_factory
from sqlalchemy import select, func
from models import User, Base, Item


class ORM:
    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_users():
        user_tom = User(login="Tom", password="pass")
        user_bob = User(login="Bob", password="blabla")
        async with session_factory() as session:
            session.add_all([user_tom, user_bob])
            await session.commit()

    @staticmethod
    async def get_count_users():
        async with session_factory() as session:
            stmt = select(func.count(User.id))
            result = await session.execute(stmt)
            return result.scalar_one()

    @staticmethod
    async def insert_items():
        item_ball = Item(name="Ball", user_id=1)
        item_car = Item(name="Car", user_id=1)
        item_tv = Item(name="TV", user_id=2)
        item_picture = Item(name="Picture", user_id=1)
        async with session_factory() as session:
            session.add_all([item_ball, item_car, item_tv, item_picture])
            await session.commit()

    @staticmethod
    async def get_password_user(login):
        async with session_factory() as session:
            stmt = select(User.password).where(User.login == login)
            result = await session.execute(stmt)
            return result.scalar_one()
