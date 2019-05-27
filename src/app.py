from flask import Flask, request, Response, make_response, session, render_template, jsonify
from flask_cors import CORS
from json import dumps, loads
from src.service import service
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'FLASK SECRET KEY'
CORS(app)

fields = {
    'username': 'string',
    'pwd': 'string',
    'email': 'string',
    'nickname': 'string',
    'register_date': 'datetime',
}
create_required_fields = ['username', 'pwd', 'email', 'nickname']
update_required_fields = ['pwd', 'nickname']

service = service.Service()

@app.route("/", methods=['GET'])
def home():
    # if 'username' not in session:
    #     session['username'] = 'test_user'
    return render_template('index.html'), 200

@app.route("/contact/", methods=['GET'])
def contact():
    return render_template('contact.html'), 200

# board and todo routes
@app.route('/todos/<int:nowpage>', methods=['GET'])
@app.route('/boards/<int:nowpage>', methods=['GET'])
def boards(nowpage=1):
    col_name = 'boards'
    subject = 'Board List'

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo List'

    result = service.find({}, nowpage, col_name) # type of list
    return render_template('board/board.html', result_list=result['list'], pagination=result['pagination'], subject=subject), 200

@app.route('/todo/view/<string:id>', methods=['GET'])
@app.route('/board/view/<string:id>', methods=['GET'])
def view(id=None):
    col_name = 'boards'
    subject = 'Board View';

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo View'

    result = service.find_by_id(id, col_name)
    result['content'] = result['content']
    return render_template('board/boardView.html', result=result, subject=subject), 200

@app.route('/todo/write/', methods=['GET', 'POST'])
@app.route('/board/write/', methods=['GET', 'POST'])
def write():
    col_name = 'boards'
    subject = 'Board Write';

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo Write'

    if request.method == 'GET':
        currTime = datetime.now().strftime('%Y%m%d %H:%M:%S')
        return render_template('board/write.html', currTime=currTime, subject=subject), 200
    else:
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        result = service.create({'title': title, 'author': author, 'content': content}, col_name)
        if result is not None:
            return '1'
        else:
            return '0'

@app.route('/todo/modify/<string:id>', methods=['GET'])
@app.route('/todo/modify/', methods=['POST'])
@app.route('/board/modify/<string:id>', methods=['GET'])
@app.route('/board/modify/', methods=['POST'])
def modify(id=None):
    col_name = 'boards'
    subject = 'Board Modify';

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo Modify'

    if request.method == 'GET':
        result = service.find_by_id(id, col_name)
        result['updated'] = datetime.now().strftime('%Y%m%d %H:%M:%S')
        return render_template('board/modify.html', result=result, subject=subject), 200
    else:
        id = request.form['_id']
        title = request.form['title']
        content = request.form['content']

        result = service.update(id, {'title': title, 'content': content}, col_name)
        if result is not None:
            return result
        else:
            return None

@app.route('/todo/delete/', methods=['POST'])
@app.route('/board/delete/', methods=['POST'])
def delete():
    col_name = 'boards'

    if request.path.find('todo') >= 0:
        col_name = 'todos'

    # _id = request.values.get('_id')
    _id = request.form['_id']
    result = service.delete(_id, col_name)
    print(result)
    if result:
        return '1'
    else:
        return '0'

# member routes
@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('user/signin.html')

@app.route('/signout/', methods=['GET'])
def signout():
    pass

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        currTime = datetime.now().strftime('%Y%m%d %H:%M:%S')
        return render_template('user/signup.html', currTime=currTime)
    else:
        pass

@app.route('/delete_account/', methods=['GET', 'POST'])
def delete_account():
    if request.method == 'GET':
        pass
    else:
        pass

# error routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 200

@app.errorhandler(500)
def server_side_error(error):
    return render_template('error/500.html'), 200

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()






# @app.route('/todos/<string:todo_id>/', methods=['GET'])
# def get_task(todo_id):
#     # 입력받은 아이디에 해당하는 도큐먼트를 find 해서(결과는 dict 타입)
#     # 반환을 위해 json byte 타입으로 convert 한다.
#     # 그것을 Response 객체에 담아서
#     # 헤더정보 및 기타정보를 세팅한 후
#     # make_response 함수로 반환한다.
#     ## ...사실 jsonify 를 활용하면 더 간단함
#     print(type(todo.find_by_id(todo_id)))
#     result = dumps(todo.find_by_id(todo_id))
#     res = Response(response=result)
#
#     for key in res.headers.keys(): # Response 객체의 header 정보 확인
#         print(key, ' : ', res.headers.get(key))
#     # res.headers.add('Contest-Type', 'application/json')
#     res.headers['Content-Type'] = 'application/json'
#     print('='*20)
#     for key in res.headers.keys(): # Response 객체의 header 정보 확인
#         print(key, ' : ', res.headers.get(key))
#
#     print('=' * 20)
#     print(res.response) # 위에서 담은 response 정보 확인
#     print(type(res.response)) # 본래 result 정보는 dict 타입이였는데, response 라는 list 내부에 담긴다.
#
#     print('=' * 20)
#     resultList = res.response[0] # list 에서 본래의 dict 정보 추출. 아직은 json byte 타입이다.
#     print(resultList)
#     resultList = loads(resultList) # json byte 타입을 호환 dict 타입으로 변환
#     print(resultList)
#     for key in resultList.keys(): # dict key-value 데이터 확인
#         print(key, ':', resultList.get(key))
#
#     ## return jsonify(todo.find_by_id(todo_id)), 200 # 그냥 단번에 jsonify 를 쓰면 됨. 템플릿이 있다면 그것으로 감싸고.
#     return make_response(res), 200
#
# @app.route('/todos/<string:todo_id>/', methods=['PUT'])
# def update_tasks(todo_id):
#     if request.method == "PUT":
#         title = request.form['title']
#         body = request.form['body']
#         response = todo.update(todo_id, {'title': title, 'body': body})
#         return response, 201
#
# @app.route('/todos/<string:todo_id>/', methods=['DELETE'])
# def delete_tasks(todo_id):
#     if request.method == "DELETE":
#         todo.delete(todo_id)
#         return "Record Deleted"



