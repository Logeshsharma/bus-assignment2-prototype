from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Group, Task, GroupTaskStatus
import datetime


def reset_db():
    db.drop_all()
    db.create_all()
    # ------Users created, added, committed to db-----
    # # g1 = Group()
    # # g2 = Group()
    # db.session.add_all([g1,g2])
    # db.session.commit()

    a = User(username='Mashrur', student_id=10, email='m@m.com', role='Admin', password_hash=generate_password_hash('mashrur.pw'), registered=True)

    u1 = User(username='amy', student_id=5, email='amy@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u2 = User(username='tom', student_id=4, email='tom@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u3 = User(username='yin', student_id=3, email='yin@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u4 = User(username='tariq', student_id=2,email='tariq@b.com',role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u5 = User(username='jo', student_id=1, email='jo@b.com',role='Mentor', password_hash=generate_password_hash('amy.pw'), registered=True)

    u6 = User(username='bob', student_id=15, email='bob@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u7 = User(username='alan', student_id=69, email='lol@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u8 = User(username='ben', student_id=420, email='xd@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=True)

    u9 = User(username='gwen', student_id=3290, email='pphead@b.com', role='Student',password_hash=generate_password_hash('amy.pw'), registered=True)

    u10 = User(username='max', student_id=56, email='ghosface@b.com', role='Mentor',password_hash=generate_password_hash('amy.pw'), registered=True)

    db.session.add_all([a, u1, u2, u3, u4, u5, u6, u7, u8, u9, u10])
    db.session.commit()



    # # g1.users.extend([u1, u2, u3, u4, u5])
    # # g2.users.extend([u6, u7, u8, u9, u10])
    #
    # db.session.commit()
    #
    # t1 = Task(title="Meet frens", description="Go outside and touch grass with some people", isUpload=True)
    # t2 = Task(title="Visit uni", description="Go outside and visit uni", isUpload=True)
    # t3 = Task(title="Visit fair", description="Meet people at the fair", isUpload=False)
    #
    # db.session.add_all([t1,t2,t3])
    # db.session.commit()
    #
    # for group in db.session.scalars(db.select(Group)):
    #     for task in db.session.scalars(db.select(Task)):
    #         group_status = GroupTaskStatus(group_id=group.id, task_id=task.id)
    #         db.session.add(group_status)
    #         db.session.commit()
