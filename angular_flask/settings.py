import tempfile
import os.path

DEBUG = True
SECRET_KEY = 'temporary_secret_key'  # make sure to change this

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('f:\code\\angular-flask', 'angular_flask.db')

print(SQLALCHEMY_DATABASE_URI)
