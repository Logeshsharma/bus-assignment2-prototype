from app import db
from app.models import User, Group
import datetime


def reset_db():
    db.drop_all()
    db.create_all()
    # ------Users created, added, committed to db-----
    g1 = Group(name = 'Group1')

    u1 = User(username='amy', email='amy@b.com', role='Admin')
    u1.set_password('amy.pw')
    u2 = User(username='tom', email='tom@b.com', role='Student')
    u2.set_password('amy.pw')
    u3 = User(username='yin', email='yin@b.com', role='Admin')
    u3.set_password('amy.pw')
    u4 = User(username='tariq', email='tariq@b.com',role='Student')
    u4.set_password('amy.pw')
    u5 = User(username='jo', email='jo@b.com',role='Mentor')
    u5.set_password('amy.pw')


    g1.users.extend([u1, u2, u3, u4, u5])
    db.session.add(g1)
    db.session.commit()
