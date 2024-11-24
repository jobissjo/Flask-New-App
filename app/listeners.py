from sqlalchemy.event import listens_for
from app.models.user import User
from app.models.profile import Profile 
from app import db

@listens_for(User, 'after_insert')
def create_profile(mapper, connection, target):
    print(target)
    profile = Profile(user_id=target.id)
    db.session.add(profile)
    db.session.commit()