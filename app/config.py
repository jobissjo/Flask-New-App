import os 
from datetime import timedelta

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-guess-if-you-try'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///db.sqlite'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  BASE_UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
  MAX_CONTENT_LENGTH = 5 * 1024 * 1024
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

  UPLOADS = {
    'avatar': {
      'max_size': 5 * 1024 * 1024,
      'allowed_extensions': ['jpg', 'png', 'jpeg'], 
      'path': os.path.join(BASE_UPLOAD_FOLDER, 'avatar')
    }
  }
  