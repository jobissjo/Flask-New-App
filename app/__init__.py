from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt

def create_app():
  
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  bcrypt.init_app(app)

  with app.app_context():
    db.create_all()

  return app
