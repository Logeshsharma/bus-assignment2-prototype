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
    a = User(username='Mashrur', student_id=1, email='mashrur@student.bham.ac.uk', role='Admin',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u1 = User(username='amy', student_id=1111111, email='amy@student.bham.ac.uk', role='Student',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u2 = User(username='tom', student_id=2222222, email='tom@student.bham.ac.uk', role='Student', registered=True)

    u3 = User(username='yin', student_id=3333333, email='yin@student.bham.ac.uk', role='Admin',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u4 = User(username='tariq', student_id=4444444, email='tariq@student.bham.ac.uk', role='Student', registered=True)

    u5 = User(username='jo', student_id=5555555, email='jo@bstudent.bham.ac.uk', role='Mentor',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u6 = User(username='bob', student_id=6666666, email='bob@student.bham.ac.uk', role='Admin',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u7 = User(username='lol', student_id=7777777, email='lol@student.bham.ac.uk', role='Student', registered=True)

    u8 = User(username='xd', student_id=8888888, email='xd@student.bham.ac.uk', role='Admin',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u9 = User(username='pphead', student_id=9999999, email='pphead@student.bham.ac.uk', role='Student',
              registered=False)

    u10 = User(username='ghostface', student_id=1000000, email='ghosface@student.bham.ac.uk', role='Mentor',
               password_hash=generate_password_hash('amy.pw'), registered=True)

    u9 = User(username='gwen', student_id=3290, email='pphead@b.com', role='Student',
              password_hash=generate_password_hash('amy.pw'), registered=True)

    u10 = User(username='max', student_id=56, email='ghosface@b.com', role='Mentor',
               password_hash=generate_password_hash('amy.pw'), registered=True)

    db.session.add_all([a, u1, u2, u3, u4, u5, u6, u7, u8, u9, u10])
    db.session.commit()

    t1 = Task(title="Meet frens", description="Go outside and touch grass with some people", isUpload=True,
              start_datetime=datetime.datetime.now() + datetime.timedelta(minutes=10),
              end_datetime=datetime.datetime.now() + datetime.timedelta(minutes=20), location="CS Building")
    t2 = Task(title="Visit uni", description="Go outside and visit uni", isUpload=True,
              start_datetime=datetime.datetime.now() + datetime.timedelta(days=1),
              end_datetime=datetime.datetime.now() + datetime.timedelta(days=2), location="Library")
    t3 = Task(title="Visit fair", description="Meet people at the fair", isUpload=False,
              start_datetime=datetime.datetime.now() + datetime.timedelta(weeks=1),
              end_datetime=datetime.datetime.now() + datetime.timedelta(weeks=2), location="Main Hall")

    db.session.add_all([t1, t2, t3])
    db.session.commit()

    for group in db.session.scalars(db.select(Group)):
        for task in db.session.scalars(db.select(Task)):
            group_status = GroupTaskStatus(group_id=group.id, task_id=task.id)
            db.session.add(group_status)
            db.session.commit()
