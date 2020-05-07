from flask import Flask  # import flask class
from config import Config # from config module import Config class
from flask_sqlalchemy import SQLAlchemy # from sqlalchemy module import SQAlchemy object
from flask_migrate import Migrate #import Migrate class from migrate package
from flask_login import LoginManager, login_required 

app = Flask(__name__) # instantiate flask object
app.config.from_object(Config) # read and apply config file
db = SQLAlchemy(app) # db object to represent the database
migrate = Migrate(app, db) # migrate object to represent Migrate engine
login = LoginManager(app) #Initialize flask login module 
login.login_view = 'login' # url_for endpoint for login view 

from app import routes, models # import routes, models file, always have this below

