from flask import Flask, g, render_template, request, jsonify, session, logging
from flask_cors import CORS
from src.model.account_form import SignupForm, SigninForm
# from src.factory.mariadb import autocomplete_result
from src.service import autocomplete_service
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db41d52ddb10d0b0ae411715154cd845'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
CORS(app)
logging.create_logger(app)

auto_service = autocomplete_service.Autocomplete_service()

@app.before_request
def before_request():
    account_form = [SignupForm(), SigninForm()]
    g.account_form = account_form

@app.route("/", methods=['GET'])
def home():
    session.permanent = True;
    return render_template('index.html', account_form=g.account_form), 200

@app.route("/contact/", methods=['GET'])
def contact():
    return render_template('contact.html', account_form=g.account_form), 200

@app.route("/autocomplete", methods=['POST'])
def autocomplete():
    query = request.form['query']
    # result = autocomplete_result(query) # return tuple type data
    # result = auto_service.find({'name': {'$regex': query}})
    result = auto_service.find({'Name': {'$regex': query, '$options': 'i'}})
    print(result)

    return jsonify({'suggestions': result})

@app.route('/search', methods=['POST'])
def search():
    word = request.values.get('word')
    result = auto_service.find_one({'Name': {'$regex': word, '$options': 'i'}})
    print(result)

    return jsonify({'result': result})

# error routes
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('error/404.html'), 200

@app.errorhandler(500)
def server_side_error(error):
    app.logger.error(error)
    return render_template('error/500.html'), 200

from src.routes import boards, members

