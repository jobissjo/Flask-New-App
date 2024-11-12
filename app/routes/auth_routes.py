from flask import Blueprint, request, jsonify
from app.schemas.auth_schema import UserSchema
from app.services.auth_service import create_user

auth_router = Blueprint("auth", __name__)

@auth_router.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    user_schema = UserSchema()

    errors = user_schema.validate(data)

    if errors:
        return jsonify(errors), 400
    
    
    user, error, status_code = create_user(data)

    if error:
        return jsonify(error), status_code
    

    return user_schema.dumb(user), 201