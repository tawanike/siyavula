import os

class Config(object):
  FLASK_RUN_HOST='0.0.0.0'
  FLASK_RUN_PORT = 8000
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = 'postgresql://siyavula:siyavula@0.0.0.0:5432/siyavula'