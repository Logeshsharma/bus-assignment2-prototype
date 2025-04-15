from datetime import timedelta

import random
from werkzeug.security import generate_password_hash

from app import db
from app.models import User, Group, Task, GroupTaskStatus, Message
import datetime


def reset_db():
    db.drop_all()
    db.create_all()
    # ------Users created, added, committed to db-----
    g1 = Group()
    g2 = Group()
    db.session.add_all([g1,g2])
    db.session.commit()

    u1 = User(username='amy', email='amy@student.bham.ac.uk', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u2 = User(username='tom', student_id=2222222, email='tom@student.bham.ac.uk', role='Student', registered=False, group_id=1)

    u3 = User(username='yin', email='yin@student.bham.ac.uk', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u4 = User(username='tariq', student_id=4444444,email='tariq@student.bham.ac.uk',role='Student', registered=False, group_id=1)

    u5 = User(username='jo', student_id=5555555, email='jo@bstudent.bham.ac.uk',role='Mentor', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=1)

    u6 = User(username='bob', email='bob@student.bham.ac.uk', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)

    u7 = User(username='lol', student_id=7777777, email='lol@student.bham.ac.uk', role='Student', registered=False, group_id=2)

    u8 = User(username='xd', email='xd@student.bham.ac.uk', role='Admin', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)

    u9 = User(username='pphead', student_id=9999999, email='pphead@student.bham.ac.uk', role='Student', registered=False, group_id=2)

    u10 = User(username='ghostface', student_id=1000000, email='ghosface@student.bham.ac.uk', role='Mentor', password_hash=generate_password_hash('amy.pw'), registered=True, group_id=2)



    g1.users.extend([u1, u2, u3, u4, u5])
    g2.users.extend([u6, u7, u8, u9, u10])

    db.session.commit()

    t1 = Task(title="Meet frens", description="Go outside and touch grass with some people", isUpload=True, start_datetime=datetime.datetime.now() + datetime.timedelta(minutes=10), end_datetime=datetime.datetime.now() + datetime.timedelta(minutes=20), location="CS Building")
    t2 = Task(title="Visit uni", description="Go outside and visit uni", isUpload=True, start_datetime=datetime.datetime.now() + datetime.timedelta(days=1), end_datetime=datetime.datetime.now() + datetime.timedelta(days=2), location="Library")
    t3 = Task(title="Visit fair", description="Meet people at the fair", isUpload=False, start_datetime=datetime.datetime.now() + datetime.timedelta(weeks=1), end_datetime=datetime.datetime.now() + datetime.timedelta(weeks=2), location="Main Hall")

    db.session.add_all([t1,t2,t3])
    db.session.commit()

    for group in db.session.scalars(db.select(Group)):
        for task in db.session.scalars(db.select(Task)):
            group_status = GroupTaskStatus(group_id=group.id, task_id=task.id)
            db.session.add(group_status)
            db.session.commit()
    def generate_random_time():
        return datetime.datetime.now() + datetime.timedelta(seconds=random.randrange(1, 9999999))

    db.session.add_all([
    Message(sent_time=generate_random_time(), content="Sample message #1 from user 1 in group 1", group_id=1, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #2 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #3 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #4 from user 7 in group 1", group_id=1, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #5 from user 6 in group 2", group_id=2, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #6 from user 8 in group 1", group_id=1, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #7 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #8 from user 6 in group 2", group_id=2, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #9 from user 6 in group 1", group_id=1, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #10 from user 3 in group 2", group_id=2, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #11 from user 1 in group 2", group_id=2, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #12 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #13 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #14 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #15 from user 10 in group 1", group_id=1, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #16 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #17 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #18 from user 3 in group 1", group_id=1, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #19 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #20 from user 3 in group 1", group_id=1, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #21 from user 3 in group 2", group_id=2, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #22 from user 6 in group 1", group_id=1, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #23 from user 1 in group 1", group_id=1, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #24 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #25 from user 10 in group 2", group_id=2, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #26 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #27 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #28 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #29 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #30 from user 6 in group 2", group_id=2, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #31 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #32 from user 3 in group 2", group_id=2, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #33 from user 4 in group 1", group_id=1, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #34 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #35 from user 4 in group 1", group_id=1, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #36 from user 10 in group 2", group_id=2, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #37 from user 3 in group 1", group_id=1, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #38 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #39 from user 4 in group 2", group_id=2, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #40 from user 9 in group 1", group_id=1, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #41 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #42 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #43 from user 9 in group 1", group_id=1, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #44 from user 1 in group 2", group_id=2, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #45 from user 4 in group 2", group_id=2, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #46 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #47 from user 9 in group 1", group_id=1, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #48 from user 4 in group 1", group_id=1, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #49 from user 8 in group 1", group_id=1, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #50 from user 10 in group 2", group_id=2, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #51 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #52 from user 4 in group 2", group_id=2, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #53 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #54 from user 1 in group 1", group_id=1, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #55 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #56 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #57 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #58 from user 10 in group 2", group_id=2, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #59 from user 9 in group 1", group_id=1, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #60 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #61 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #62 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #63 from user 6 in group 1", group_id=1, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #64 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #65 from user 3 in group 1", group_id=1, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #66 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #67 from user 5 in group 2", group_id=2, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #68 from user 5 in group 1", group_id=1, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #69 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #70 from user 5 in group 2", group_id=2, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #71 from user 9 in group 2", group_id=2, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #72 from user 4 in group 2", group_id=2, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #73 from user 10 in group 1", group_id=1, user_id=10),
    Message(sent_time=generate_random_time(), content="Sample message #74 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #75 from user 5 in group 2", group_id=2, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #76 from user 1 in group 1", group_id=1, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #77 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #78 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #79 from user 3 in group 2", group_id=2, user_id=3),
    Message(sent_time=generate_random_time(), content="Sample message #80 from user 7 in group 1", group_id=1, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #81 from user 4 in group 2", group_id=2, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #82 from user 6 in group 2", group_id=2, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #83 from user 1 in group 1", group_id=1, user_id=1),
    Message(sent_time=generate_random_time(), content="Sample message #84 from user 7 in group 1", group_id=1, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #85 from user 5 in group 2", group_id=2, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #86 from user 2 in group 1", group_id=1, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #87 from user 6 in group 1", group_id=1, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #88 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #89 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #90 from user 5 in group 2", group_id=2, user_id=5),
    Message(sent_time=generate_random_time(), content="Sample message #91 from user 7 in group 1", group_id=1, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #92 from user 7 in group 2", group_id=2, user_id=7),
    Message(sent_time=generate_random_time(), content="Sample message #93 from user 4 in group 1", group_id=1, user_id=4),
    Message(sent_time=generate_random_time(), content="Sample message #94 from user 8 in group 1", group_id=1, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #95 from user 6 in group 1", group_id=1, user_id=6),
    Message(sent_time=generate_random_time(), content="Sample message #96 from user 8 in group 2", group_id=2, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #97 from user 2 in group 2", group_id=2, user_id=2),
    Message(sent_time=generate_random_time(), content="Sample message #98 from user 8 in group 1", group_id=1, user_id=8),
    Message(sent_time=generate_random_time(), content="Sample message #99 from user 9 in group 1", group_id=1, user_id=9),
    Message(sent_time=generate_random_time(), content="Sample message #100 from user 5 in group 1", group_id=1, user_id=5)])
    db.session.commit()
