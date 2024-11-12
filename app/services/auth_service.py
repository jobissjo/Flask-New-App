from app.models.user import User
from .. import db, bcrypt 


def create_user(data):
    username = data.get('username')
    email = data.get('email')

    if User.query.filter_by(username=username). first():
        return None, "username already exists", 400

    
    if User.query.filter_by(email=email).first ():
        return None, "email already exists", 400
    
    
    hashed_password = bcrypt.generate_password_hash(data['passwoed']).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user, None, 200