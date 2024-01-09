from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from orm import ORM


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        login, password = form["username"], form["password"]

        if password == await ORM.get_password_user(login):
            request.session.update({"token": "..."})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        return True


authentication_backend = AdminAuth(secret_key="...")
