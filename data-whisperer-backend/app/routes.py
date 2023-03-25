from flask import jsonify
from . import app
from .models import Customer, Order, Payment
from .schemas import CustomerSchema, OrderSchema, PaymentSchema

customers_schema = CustomerSchema(many=True)
orders_schema = OrderSchema(many=True)
payments_schema = PaymentSchema(many=True)


@app.route('/api/v1/customers', methods=['GET'])
def get_customers():
    all_customers = Customer.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result)

@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)

@app.route('/api/v1/payments', methods=['GET'])
def get_payments():
    all_payments = Payment.query.all()
    result = payments_schema.dump(all_payments)
    return jsonify(result)
