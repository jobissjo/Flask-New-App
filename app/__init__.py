from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

bcrypt = Bcrypt()
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Import routes after db initialization to avoid circular imports
    from app.routes.auth_routes import auth_router
    from app.routes.profile_routes import profile_router

    app.register_blueprint(auth_router, url_prefix='/api/auth')
    app.register_blueprint(profile_router, url_prefix='/api/profile')

    return app
