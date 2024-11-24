# Standard Library Imports
# (None in this case)
from datetime import datetime

# Third-party Imports
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local Imports
from app.services.profile_service import get_or_create_profile_by_user_id, update_current_profile
from app.utils.file_uploads import save_file
from app.models.profile import Profile
from app.schemas.profile_schemas import ProfileUpdateSchema


profile_schema = ProfileUpdateSchema()
profile_router = Blueprint('profile', __name__)


@profile_router.route('/edit', methods=['PUT'])
@jwt_required()
def edit_profile():
    try:
        current_user_id = int(get_jwt_identity())
        file = request.files.get('avatar')
        data = request.form.to_dict()

        profile, _ = get_or_create_profile_by_user_id(current_user_id)

        
        if file:
            profile.avatar_url = save_file(file, current_app.config['UPLOADS']['avatar'])
        if dob:=data.get('dob', None):
            data.update({'dob': datetime.strptime(dob, "%Y-%m-%d").date()})
            print(data['dob'])
        update_current_profile(profile, data)

        return jsonify({'message': 'Profile updated successfully', 'data': profile.to_dict()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@profile_router.route('/update-avatar', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()

    file = request.files.get('avatar')

    profile, _ = get_or_create_profile_by_user_id(current_user_id)
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    
    if file:
        profile.avatar_url = save_file(file, current_app.config['UPLOADS']['avatar'])
      
    return jsonify({'message': 'Profile Avatar updated successfully', 'data': profile.to_dict()}), 200