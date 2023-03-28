from .models import Customer
from marshmallow import fields
from marshmallow.validate import Length
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True

    first_name = fields.Str(required=True, validate=Length(max=100))
    last_name = fields.Str(required=True, validate=Length(max=100))