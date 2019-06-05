from flask import render_template, url_for, request, session, flash, redirect
from datetime import datetime
from json import dumps
from src import app
from src.service import board_service

b_service = board_service.Board_service()

# board and todo routes
@app.route('/todos/', methods=['GET', 'POST'])
@app.route('/boards/', methods=['GET', 'POST'])
def boards():
    col_name = 'boards'
    subject = 'Board List'
    nowpage = 1

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo List'

    if request.method == 'POST':
        nowpage = int(request.form['nowpage'])
        result = b_service.find({}, nowpage, col_name) # type of list
        return dumps(render_template('board/list.html', result_list=result['list'], pagination=result['pagination'], subject=subject))

    result = b_service.find({}, nowpage, col_name) # type of list
    return render_template('board/board.html', result_list=result['list'], pagination=result['pagination'], subject=subject), 200

@app.route('/todo/view/<string:id>', methods=['GET'])
@app.route('/board/view/<string:id>', methods=['GET'])
def view(id=None):
    col_name = 'boards'
    subject = 'Board View';

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo View'

    result = b_service.find_by_id(id, col_name)
    return render_template('board/view.html', result=result, subject=subject), 200

@app.route('/todo/write/', methods=['GET', 'POST'])
@app.route('/board/write/', methods=['GET', 'POST'])
def write():
    col_name = 'boards'
    subject = 'Board Write';

    if request.path.find('todo') >= 0:
        col_name = 'todos'
        subject = 'Todo Write'

    if request.method == 'GET':
        if 'email' in session:
            currTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return render_template('board/write.html', currTime=currTime, subject=subject), 200
        else:
            flash(f'You have to SIGN IN first', 'info')
            return redirect(url_for('signin'))
    else:
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        result = b_service.create({'title': title, 'author': author, 'content': content}, col_name)
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
        result = b_service.find_by_id(id, col_name)
        result['updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return render_template('board/modify.html', result=result, subject=subject), 200
    else:
        id = request.form['_id']
        title = request.form['title']
        content = request.form['content']

        result = b_service.update(id, {'title': title, 'content': content}, col_name)
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
    result = b_service.delete(_id, col_name)
    print(result)
    if result:
        return '1'
    else:
        return '0'