from app import app
from flask_socketio import SocketIO

socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')

if __name__ == '__main__':
    socketio.run(app, debug=True)
