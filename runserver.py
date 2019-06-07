from src import app
from src.model import connection_count
from flask import session
from flask_socketio import SocketIO, send, emit
from datetime import datetime

socketio = SocketIO(app)
conn_count = connection_count.Connection_count()

@socketio.on("connect", namespace="/timeline")
def connect():
    if 'nickname' in session:
        conn_count.add_conn(1)
        emit('response', {'stat': 'connect', 'data': 'New Member', 'nickname': session['nickname'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)
    else:
        conn_count.add_conn(2)
        session['guest_num'] = str(conn_count.get_guest())
        emit('response', {'stat': 'connect', 'data': 'New Guest', 'nickname': 'guest' + session['guest_num'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)

@socketio.on("request", namespace="/timeline")
def request(timeline):
    print("timeline : " + timeline['data'])
    if 'nickname' in session:
        emit('response', {'stat': 'request', 'data': timeline['data'], 'nickname': session['nickname'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)
    else:
        emit('response', {'stat': 'request', 'data': timeline['data'], 'nickname': 'guest' + session['guest_num'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)

@socketio.on("disconnect", namespace="/timeline")
def disconnect():
    print('disconnected')
    if 'nickname' in session:
        conn_count.sub_conn()
        emit('response', {'stat': 'disconnect', 'data': 'Disconnected', 'nickname': session['nickname'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)
    else:
        conn_count.sub_conn()
        emit('response', {'stat': 'disconnect', 'data': 'Disconnected', 'nickname': 'guest' + session['guest_num'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)
    session.clear()

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()

