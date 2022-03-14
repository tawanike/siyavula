import os

class Config(object):
  PORT = 8000
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = 'postgresql://siyavula:siyavula@db/siyavula'