from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app():
  
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  bcrypt.init_app(app)

  from app.routes.auth_routes import auth_router

  app.register_blueprint(auth_router, url_prefix='/api')

  return app
