import os
import requests
import sys

from contextlib import contextmanager, redirect_stdout
import re

import io
from contextlib import redirect_stdout
import mock
from flask import request, jsonify
from sqlalchemy import inspect
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from flask_socketio import emit

from . import app
from .models import Customer, Order, Payment, db
from .schemas import CustomerSchema, OrderSchema, PaymentSchema

@contextmanager
def st_capture(output_function):
    with io.StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write

        def new_write(string):
            ret = old_write(string)
            output_function(escape_ansi(stdout.getvalue()))
            return ret

        stdout.write = new_write
        yield

def escape_ansi(line):
    return re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]').sub('', line)


# Get the absolute path of the current file
base_path = os.path.abspath(os.path.dirname(__file__))

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

@app.route('/api/v1/tables', methods=['GET'])
def get_tables():
    inspector = inspect(db.engine)
    table_names = inspector.get_table_names()
    return jsonify(table_names)

@app.route('/api/v1/run', methods=['POST'])
def run():
    # Construct the absolute path of the database file
    db_path = os.path.join(base_path, '..', 'sqlite_db', 'my_database.db')

    # Create the database connection
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    toolkit = SQLDatabaseToolkit(db=db)

    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0),
        toolkit=toolkit,
        verbose=True
    )

    request_data = request.get_json()
    command = request_data.get("command", "")

    def emit_print(*args, **kwargs):
        message = " ".join(str(a) for a in args)

        # Use the escape_ansi function to remove ANSI escape codes before emitting the message
        escaped_message = escape_ansi(message)

        emit('output', {'message': escaped_message}, namespace='/', broadcast=True)
        sys.stdout.write(escaped_message + "\n")
        sys.stdout.flush()

    with mock.patch('builtins.print', emit_print):
        agent_executor.run(command)

    return jsonify({'running': command})