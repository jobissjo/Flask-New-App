from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.users import User

auth_router = Blueprint("auth", __name__)

@auth_router.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not username or not email or not password:
        return jsonify({"message": "username, email and password are required field"})

    if User.query.filter_by(username=username). first():
        return jsonify({"message": "username already exists"})

    if User.valid_email(email):
        return jsonify({"message": "email is not valid"})

    if User.query.filter_by(email=email).first ():
        return jsonify({"message": "email already exists"})

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "user created successfully"})