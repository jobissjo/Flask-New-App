from flask import Blueprint, request, jsonify
from app.schemas.auth_schema import UserSchema, UserBasicSchema
from app.services.auth_service import create_user, authenticate_user, get_user_by_user_id
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

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


@auth_router.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    email = data.get('email')

    password = data.get('password')
    
    user = authenticate_user(email, password)

    if not user:
        return jsonify({"message": "Invalid credentials"}),400

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


@auth_router.route('/get_current_user', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        current_user_id =get_jwt_identity()
        user_detail = get_user_by_user_id(current_user_id)
        user_data = UserBasicSchema.dump(user_detail)
        return jsonify({'user': user_data}), 200
    except Exception as e:
        return jsonify({'error':str(e)}), 400