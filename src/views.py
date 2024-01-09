from sqladmin import ModelView
from models import User, Item


class UserAdmin(ModelView, model=User):
    can_create = True
    column_exclude_list = [User.password]
    column_details_exclude_list = [User.password]
    list_template = "user.html"


class ItemAdmin(ModelView, model=Item):
    can_create = True
    column_list = "__all__"
    list_template = "item.html"
