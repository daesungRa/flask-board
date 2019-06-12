from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Required, Length, Email, EqualTo, ValidationError
from src.factory.database import Database

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    pwd = PasswordField('Password', validators=[DataRequired()])
    confirm_pwd = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('pwd')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=2, max=20)])
    profile = FileField('Profile', validators=[FileAllowed(['jpg', 'png']), FileRequired()])
    #recaptcha = RecaptchaField(validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        db = Database()
        criteria = {'email': email.data}
        user = db.find_one(criteria=criteria, collection_name='members', projection=['email', 'nickname'])
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')

    def validate_nickname(self, nickname):
        db = Database()
        criteria = {'nickname': nickname.data}
        user = db.find_one(criteria=criteria, collection_name='members', projection=['email', 'nickname'])
        if user:
            raise ValidationError('That nickname is already taken. Please choose a different one.')

    # https://stackoverflow.com/questions/52899084/flask-wtforms-why-is-my-post-request-to-upload-a-file-not-sending-the-file-data

class SigninForm(FlaskForm):
    pwd = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    remember = BooleanField('Remember Me')
    #recaptcha = RecaptchaField(validators=[DataRequired()])
    submit = SubmitField('Sign In')


