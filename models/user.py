from tortoise import fields
from tortoise.filters import not_null
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(max_length = 50)
    username = fields.CharField(max_length = 150, unique = True)
    email = fields.CharField(max_length = 100, unique = True)
    created_at = fields.DateField(auto_now_add = True)