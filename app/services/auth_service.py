from app.models.user import User
from .. import db, bcrypt


def create_user(data):
    username = data.get("username")
    email = data.get("email")

    # Check for existing username or email
    if User.query.filter_by(username=username).first():
        return None, "username already exists", 400

    if User.query.filter_by(email=email).first():
        return None, "email already exists", 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return new_user, None, 200


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None


def get_user_by_user_id(user_id):
    return User.query.get(user_id)
