# Web Form Classes files
from flask_wtf import FlaskForm # import form class from flask_wtf 
from wtforms import StringField, PasswordField, BooleanField, SubmitField # import field types
from wtforms.validators import DataRequired # import validation behaviors

# Define the Login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')