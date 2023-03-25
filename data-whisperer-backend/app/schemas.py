from . import ma
from .models import User
from marshmallow_sqlalchemy import auto_field

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('id', 'name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
