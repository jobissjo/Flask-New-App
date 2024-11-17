from app.models.profile import Profile
from app import db

def get_profile_by_user_id(user_id):
    return Profile.query.filter_by(user_id=user_id).first()

def update_profile(profile, data):
    for key, value in data.items():
        setattr(profile, key, value)

    db.session.commit()
    