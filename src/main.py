import asyncio
import uvicorn
from sqladmin import Admin
from orm import ORM
from database import engine
import fastapi
from fastapi.responses import RedirectResponse
from views import UserAdmin, ItemAdmin
from auth import authentication_backend


async def manipulate_db():
    await ORM.create_tables()
    await ORM.insert_users()
    await ORM.insert_items()


def create_fastapi():
    app = fastapi.FastAPI()

    @app.get("/")
    def redirect():
        response = RedirectResponse(url='/admin')
        return response

    return app


appl = create_fastapi()
admin = Admin(appl, engine, templates_dir="src/templates", authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(ItemAdmin)

if __name__ == '__main__':
    asyncio.run(manipulate_db())
    create_fastapi()
    uvicorn.run("main:appl", reload=True)
