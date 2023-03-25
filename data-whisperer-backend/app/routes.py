from flask import jsonify
from . import app
from .models import User
from .schemas import users_schema

@app.route('/api/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)
