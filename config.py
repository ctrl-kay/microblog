# Config class to set and store variables #

import os
basedir = os.path.abspath(os.path.dirname(__file__)) #base directory variable

# Look for value of SECRET_KEY enviroment variable,  or use hard coded string #
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # secret key variable

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db') #if variable not defined,use app.db in main directory
		# which is stored in the basedir
	SQLALCHEMY_TRACK_MODIFICATIONS = False # stop signaling app when db is updated
