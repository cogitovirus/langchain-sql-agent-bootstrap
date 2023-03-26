import os
import requests
import sys

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
    # API_KEY = os.environ['OPENAI_API_KEY']
    # API_URL = "https://api.openai.com/v1/chat/completions"

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
    # print(command)

    # return jsonify({"command": command})

    # agent_executor.run(command)

    # Wrap the print function to emit the output
    def emit_print(*args, **kwargs):
        message = " ".join(str(a) for a in args)
        emit('output', {'message': message}, namespace='/', broadcast=True)
        sys.stdout.write(message + "\n")
        sys.stdout.flush()



    with io.StringIO() as buf, redirect_stdout(buf):
        # Replace the print function with our custom function
        with mock.patch('builtins.print', emit_print):
            agent_executor.run(command)

        output = buf.getvalue()

    return jsonify({'result': output})

    # return jsonify({"command": command})

    # headers = {
    #     "Content-Type": "application/json",
    #     "Authorization": f"Bearer {API_KEY}",
    # }

    # request_data = request.get_json()
    # command = request_data.get("command", "")

    # messages = [
    #     {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    #     {"role": "user", "content": f'Translate the following English text to French: "{command}"'}
    # ]

    # data = {
    #     "model": "gpt-3.5-turbo",
    #     "messages": messages,
    #     "max_tokens": 50,
    # }

    # response = requests.post(API_URL, json=data, headers=headers)

    # if response.status_code == 200:
    #     return jsonify(response.json())
    # else:
    #     return jsonify({"error": "Error generating text"}), response.status_code