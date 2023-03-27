from .models import Customer, Order, Payment

from marshmallow import fields
from marshmallow.validate import Length
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True

    first_name = fields.Str(required=True, validate=Length(max=100))
    last_name = fields.Str(required=True, validate=Length(max=100))

class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True

    user_id = fields.Int(required=True)
    order_date = fields.Str(required=True, validate=Length(max=50))
    status = fields.Str(required=True, validate=Length(max=50))


class PaymentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Payment
        load_instance = True

    order_id = fields.Int(required=True)
    payment_method = fields.Str(required=True, validate=Length(max=100))
    amount = fields.Float(required=True)
