import os

# Config class to set and store variables #

# Look for value of SECRET_KEY enviroment variable,  or use hard coded string #
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'