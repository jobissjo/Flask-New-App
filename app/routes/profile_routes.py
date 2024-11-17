from flask import Blueprint, request, jsonify, current_app
from app.models.profile import Profile
from app import db
from app.schemas.profile_schema import ProfileSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.file_uploads import save_file

from app.services.profile_service import get_profile_by_user_id, update_profile

profile_router = Blueprint('profile', __name__)


@profile_router.route('/edit', methods=['PUT'])
@jwt_required()
def edit_profile():
    current_user_id = get_jwt_identity()['user_id']
    file = request.files.get('avatar')
    data = request.form.to_dict()

    profile = get_profile_by_user_id(current_user_id)

    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    
    if file:
        profile.avatar_url = save_file(file, current_app.config['UPLOADS']['avatar'])

    update_profile(profile, data)
    return jsonify({'message': 'Profile updated successfully'}), 200


@profile_router.route('/upldate-avatar', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_id = get_jwt_identity()['user_id']
    file = request.files.get('avatar')

    profile = get_profile_by_user_id(current_user_id)
  
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    
    if file:
        profile.avatar_url = save_file(file, current_app.config['UPLOADS']['avatar'])
      
    return jsonify({'message': 'Profile updated successfully'}), 200