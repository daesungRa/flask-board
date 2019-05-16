from flask import Flask, request, Response, make_response, render_template, jsonify
from flask_cors import CORS
from json import dumps, loads
from src.models import todo

app = Flask(__name__)
CORS(app)

todo = todo.Todo()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html'), 200

# todo routes
@app.route('/todos/', methods=['GET'])
def get_tasks():
    return jsonify(todo.find({})), 200

@app.route('/todos/<string:todo_id>/', methods=['GET'])
def get_task(todo_id):
    # 입력받은 아이디에 해당하는 도큐먼트를 find 해서(결과는 dict 타입)
    # 반환을 위해 json byte 타입으로 convert 한다.
    # 그것을 Response 객체에 담아서
    # 헤더정보 및 기타정보를 세팅한 후
    # make_response 함수로 반환한다.
    ## ...사실 jsonify 를 활용하면 더 간단함
    print(type(todo.find_by_id(todo_id)))
    result = dumps(todo.find_by_id(todo_id))
    res = Response(response=result)
    
    for key in res.headers.keys(): # Response 객체의 header 정보 확인
        print(key, ' : ', res.headers.get(key))
    # res.headers.add('Contest-Type', 'application/json')
    res.headers['Content-Type'] = 'application/json'
    print('='*20)
    for key in res.headers.keys(): # Response 객체의 header 정보 확인
        print(key, ' : ', res.headers.get(key))

    print('=' * 20)
    print(res.response) # 위에서 담은 response 정보 확인
    print(type(res.response)) # 본래 result 정보는 dict 타입이였는데, response 라는 list 내부에 담긴다.

    print('=' * 20)
    resultList = res.response[0] # list 에서 본래의 dict 정보 추출. 아직은 json byte 타입이다.
    print(resultList)
    resultList = loads(resultList) # json byte 타입을 호환 dict 타입으로 변환
    print(resultList)
    for key in resultList.keys(): # dict key-value 데이터 확인
        print(key, ':', resultList.get(key))

    ## return jsonify(todo.find_by_id(todo_id)), 200 # 그냥 단번에 jsonify 를 쓰면 됨. 템플릿이 있다면 그것으로 감싸고.
    return make_response(res), 200

@app.route('/todos/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        response = todo.create({'title': title, 'body': body})
        return response, 201

@app.route('/todos/<string:todo_id>/', methods=['PUT'])
def update_tasks(todo_id):
    if request.method == "PUT":
        title = request.form['title']
        body = request.form['body']
        response = todo.update(todo_id, {'title': title, 'body': body})
        return response, 201

@app.route('/todos/<string:todo_id>/', methods=['DELETE'])
def delete_tasks(todo_id):
    if request.method == "DELETE":
        todo.delete(todo_id)
        return "Record Deleted"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()