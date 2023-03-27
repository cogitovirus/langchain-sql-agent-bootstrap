from . import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    orders = db.relationship('Order', backref='customers', lazy=True)

    def __repr__(self):
        return f"<Customer {self.id}: {self.first_name} {self.last_name}>"

    def __init__(self, name):
        self.name = name

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    order_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # customer = db.relationship('Customer', backref='orders')

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    payment_method = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Payment {self.id}: {self.payment_method}, {self.amount}>"

    def __init__(self, name):
        self.name = name
