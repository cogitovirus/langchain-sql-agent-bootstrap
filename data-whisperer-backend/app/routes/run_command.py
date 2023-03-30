# app/routes/main.py

import os
import sys
import re
import io
from contextlib import contextmanager, redirect_stdout
import mock
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from flask_socketio import emit
from flask import request, jsonify
from flask import current_app


from . import main_blueprint

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

@main_blueprint.route('/api/v1/run-command', methods=['POST'])
def run_command():
    # Construct the absolute path of the database file
    db_path = os.path.join(base_path, '..','..','sqlite_db', 'my_database.db')

    # Create the database connection
    db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

    toolkit = SQLDatabaseToolkit(db=db)

    model_name = current_app.config['MODEL_NAME']

    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0, model_name=model_name),
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
