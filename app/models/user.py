from app import db
from email_validator import validate_email, EmailNotValidError

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"{self.username}"

    @staticmethod
    def is_valid_email(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False