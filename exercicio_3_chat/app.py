from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send, emit

# criando a aplicação ===============
app = Flask(__name__)

# configurando o socketio ================
# https://flask-socketio.readthedocs.io/en/latest/
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect(auth):
    print('connected: ', auth)

@socketio.on('disconnect')
def handle_disconnect():
    print('disconnect: ')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    #emit('message', data, broadcast=True) # envia para todos
    socketio.send(data) #envia para todos
    #send(data) devolve só para quem mandou

# definindo rotas ===============
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)