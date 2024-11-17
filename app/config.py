import os 

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-guess-if-you-try'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/db.sqlite'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  BASE_UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
  MAX_CONTENT_LENGTH = 5 * 1024 * 1024

  UPLOADS = {
    'avatar': {
      'max_size': 5 * 1024 * 1024,
      'allowed_file_types': ['jpg', 'png', 'jpeg'], 
      'path': os.path.join(BASE_UPLOAD_FOLDER, 'avatar')
    }
  }
  