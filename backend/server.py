from flask import Flask, request, make_response, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'secret!'

socket_io = SocketIO(app, cors_allowed_origins="*")

@socket_io.on('connect')
def test_connect():
    print('Client connect')

@socket_io.on('disconnect')
def test_disconnect():
    print('Client disconnect')

@socket_io.on('message')
def test_disconnect(data):
    print(str(data))
    

if __name__ == "__main__":
    socket_io.run(app, host='0.0.0.0', port=5000)