from flask import Flask, g, render_template
from flask_cors import CORS
from src.model.account_form import SignupForm, SigninForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db41d52ddb10d0b0ae411715154cd845'
CORS(app)

@app.before_request
def before_request():
    account_form = [SignupForm(), SigninForm()]
    g.account_form = account_form

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', account_form=g.account_form), 200

@app.route("/contact/", methods=['GET'])
def contact():
    return render_template('contact.html', account_form=g.account_form), 200

# error routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 200

@app.errorhandler(500)
def server_side_error(error):
    return render_template('error/500.html'), 200

from src.routes import boards, members

