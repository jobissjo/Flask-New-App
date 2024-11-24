from app.models.profile import Profile
from app import db


def get_or_create_profile_by_user_id(user_id):
    profile =  Profile.query.filter_by(user_id=user_id).first()
    if profile is None:
        profile = Profile(user_id=user_id)
        db.session.add(profile)
        db.session.commit()
        return profile, True
    return profile, False

def update_current_profile(profile, data):
    for key, value in data.items():
        setattr(profile, key, value)

    db.session.commit()
    