import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from clinicapp import db, app
from enum import Enum as RoleEnum
import hashlib
from flask_login import UserMixin



class UserRole(RoleEnum):
    ADMIN = 1
    USER = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default="https://res.cloudinary.com/dahmfjhys/image/upload/v1733907188/f57rz9849qmsthijvoxp.jpg")
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class BenhNhan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ho_ten = db.Column(db.String(100), nullable=False)
    so_dien_thoai = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class BacSi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ho_ten = db.Column(db.String(100), nullable=False)
    chuyen_khoa = db.Column(db.String(100), nullable=False)

class DatLichKham(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ho_ten = db.Column(db.String(100), nullable=False)
    ngay_kham = db.Column(db.Date, nullable=False)
    gio_kham = db.Column(db.Time, nullable=False)
    bac_si = db.Column(db.String(50), nullable=False)
    ghi_chu = db.Column(db.String(300))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(name='admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRole.ADMIN)
        db.session.add(u)
        db.session.commit()

        db.session.commit()