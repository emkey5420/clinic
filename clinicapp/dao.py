from models import User
from clinicapp import app, db , login
import hashlib






def auth_user(account, password, role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = User.query.filter(User.account.__eq__(account.strip()),
                          User.password.__eq__(password))
    if role:
        u = u.filter(User.user_role.__eq__(role))

    return u.first()


def add_user(name, account, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u = User(name=name, account=account, password=password)

    db.session.add(u)
    db.session.commit()


def get_user_by_id(id):
    return User.query.get(id)