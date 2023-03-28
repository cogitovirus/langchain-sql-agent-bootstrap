from app import create_app
from app.Config import Config
from flask_socketio import SocketIO


if __name__ == '__main__':
    app = create_app(Config)
    socketio = SocketIO(app, cors_allowed_origins='http://localhost:3000')
    socketio.run(app, debug=True)
