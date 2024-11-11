import os 

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-guess-if-you-try'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///db.sqlite'
  SQLALCHEMY_TRACK_MODIFICATIONS = False