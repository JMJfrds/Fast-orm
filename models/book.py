from tortoise import fields
from tortoise.models import  Model


class Book(Model):
    id = fields.IntField(pk = True)
    author = fields.ForeignKeyField('models.User', related_name = 'books')
    title = fields.CharField(max_length = 150, unique = True)
    description = fields.CharField(max_length = 150, unique = True)
    created_at = fields.DateField(auto_now_add = True)