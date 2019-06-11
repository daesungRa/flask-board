from flask import session
from flask_socketio import SocketIO, emit
from datetime import datetime
from src import app
from src.model import connection_count

socketio = SocketIO(app)
conn_count = connection_count.Connection_count()

@socketio.on("connect", namespace="/timeline")
def connect():
    if 'nickname' in session:
        conn_count.add_conn(1)
        response_data = {'stat': 'connect', 'data': 'New Member', 'nickname': session['nickname'], 'tot': conn_count.get_tot(), 'time': datetime.now().strftime('%H:%M:%S')}
    else:
        conn_count.add_conn(2)
        session['nickname'] = 'guest' + str(conn_count.get_guest())
        response_data = {'stat': 'connect', 'data': 'New Guest', 'nickname': session['nickname'], 'tot': conn_count.get_tot(), 'time': datetime.now().strftime('%H:%M:%S')}

    emit('response', response_data, broadcast=True)

@socketio.on("timeline", namespace="/timeline")
def timeline(timeline):
    data = timeline['data']
    nickname = timeline['nickname']
    print("[nickname]timeline : " + "[" + nickname + "]" + data)
    print(session['nickname'])

    # 타임라인 요청에 담긴 송신자의 nickname 과 현재 접속 세션의 nickname 을 비교하는 것이지만,
    # 같은 호스트 내에서 전송된 요청이라면 서로 다른 탭일지라도 구분이 불가하므로,
    # 일단은 테스트를 위해 다음과 같이 작성한다.
    # 추후 배포를 한다면, 비교 로직을 추가할 것 (nickname != session['nickname'])
    emit('response', {'stat': 'timeline', 'data': data, 'nickname': nickname, 'tot': conn_count.get_tot(), 'time': datetime.now().strftime('%H:%M')}, broadcast=True)

@socketio.on("disconnect", namespace="/timeline")
def disconnect(msg):
    print('disconnected')

    emit('disconnect', {'data': 'Disconnected', 'nickname': session['nickname'], 'time': datetime.now().strftime('%H:%M')}, broadcast=True)
    session.clear()


