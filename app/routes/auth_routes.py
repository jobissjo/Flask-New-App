from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.schemas.auth_schema import UserSchema, UserBasicSchema
from app.services.auth_service import create_user, authenticate_user, get_user_by_user_id

# Define Blueprint
auth_router = Blueprint("auth", __name__)

# Register Route
@auth_router.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    # Validate input using the schema
    user_schema = UserSchema()
    errors = user_schema.validate(data)

    if errors:
        return jsonify({'error': errors}), 400
    
    # Create the user
    user, error, status_code = create_user(data)

    if error:
        return jsonify({'error': error}), status_code
    if user:
        return jsonify({'data': user_schema.dump(user)}), 201
    return jsonify({'error': "Unknown error"}), 400


# Login Route
@auth_router.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    
    # Authenticate the user
    user = authenticate_user(email, password)

    if not user:
        return jsonify({"message": "Invalid credentials"}), 400

    # Create a JWT token
    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token}), 200


# Get current user route
@auth_router.route('/get_current_user', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        # Get the current user ID from the JWT token
        current_user_id = get_jwt_identity()
        
        # Fetch the user details from the database
        user_detail = get_user_by_user_id(current_user_id)

        if not user_detail:
            return jsonify({'error': 'User not found'}), 404
        
        # Serialize the user data
        user_data = UserBasicSchema().dump(user_detail)

        return jsonify({'user': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
