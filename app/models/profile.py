from app import db
from app.models.user import User

class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.Foreignkey('users.id'), unique=True, nullable=False)
    bio = db.Column(db.String(500), nullable=True)
    avatar_url = db.Column(db.String(500), nullable=True)

    dob = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    location = db.Column(db.String(150), nullable=True)

    user = db.relationship('User', back_populates='profile')
   