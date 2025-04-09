from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Group, Task, GroupTaskStatus
import datetime


def reset_db():
    db.drop_all()
    db.create_all()
    # ------Users created, added, committed to db-----
    g1 = Group()
    g2 = Group()
    db.session.add_all([g1,g2])
    db.session.commit()

    u1 = User(username='amy', student_id=5, email='amy@b.com', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u2 = User(username='tom', student_id=4, email='tom@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=False, group_id=1)

    u3 = User(username='yin', student_id=3, email='yin@b.com', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u4 = User(username='tariq', student_id=2,email='tariq@b.com',role='Student', password_hash=generate_password_hash('amy.pw'), registered=False, group_id=1)

    u5 = User(username='jo', student_id=1, email='jo@b.com',role='Mentor', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u6 = User(username='bob', student_id=15, email='bob@b.com', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)

    u7 = User(username='lol', student_id=69, email='lol@b.com', role='Student', password_hash=generate_password_hash('amy.pw'), registered=False, group_id=2)

    u8 = User(username='xd', student_id=420, email='xd@b.com', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)

    u9 = User(username='pphead', student_id=3290, email='pphead@b.com', role='Student',password_hash=generate_password_hash('amy.pw'), registered=False, group_id=2)

    u10 = User(username='ghostface', student_id=56, email='ghosface@b.com', role='Mentor',password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)



    g1.users.extend([u1, u2, u3, u4, u5])
    g1.users.extend([u6, u7, u8, u9, u10])

    db.session.commit()

    t1 = Task(title="Meet frens", description="Go outside and touch grass with some people", isUpload=True)
    t2 = Task(title="Visit uni", description="Go outside and visit uni", isUpload=True)
    t3 = Task(title="Visit fair", description="Meet people at the fair", isUpload=False)

    db.session.add_all([t1,t2,t3])
    db.session.commit()

    for group in db.session.scalars(db.select(Group)):
        for task in db.session.scalars(db.select(Task)):
            group_status = GroupTaskStatus(group_id=group.id, task_id=task.id)
            db.session.add(group_status)
            db.session.commit()
