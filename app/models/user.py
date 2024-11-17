from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    profile = db.relationship('Profile', back_populates='user', uselist=False)

    def __repr__(self):
        return f"{self.username}"