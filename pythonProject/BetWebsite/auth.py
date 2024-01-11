import bcrypt
from BetWebsite.db_manager import db_manager
from BetWebsite.models import User
db_manager = db_manager()
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)


def sign_up(username, email, password):
    hashed_password = hash_password(password)
    new_user = User(fullName=username, email=email, password=hashed_password)
    with db_manager as session:
        session.add(new_user)
        session.commit()


def login(username, password):
    with db_manager as session:
        user = session.query(User).filter_by(fullName=username).first()
    if user and check_password(user.password, password):
        return True
    return False
