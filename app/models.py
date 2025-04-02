from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.testing.schema import mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from dataclasses import dataclass
import datetime


@dataclass
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    role: so.Mapped[str] = so.mapped_column(sa.String(10), default="Normal")

    loans: so.Mapped[list['Loan']] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        pwh = 'None' if not self.password_hash else f'...{self.password_hash[-5:]}'
        return f'User(id={self.id}, username={self.username}, email={self.email}, role={self.role}, pwh={pwh})'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))


class Book(db.Model):
    __tablename__ = 'books'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    author: so.Mapped[str] = so.mapped_column(sa.String(120), index=True)
    genre: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), index=True)
    summary: so.Mapped[str] = so.mapped_column(sa.String(256))
    year: so.Mapped[int] = so.mapped_column()
    loan: so.Mapped['Loan'] = relationship(back_populates='book', cascade='all, delete-orphan')


class Loan(db.Model):
    date_loaned: so.Mapped[datetime] = so.mapped_column(sa.DateTime())

    book_id: so.Mapped[int] = mapped_column(ForeignKey('books.id'), index=True, primary_key=True)
    book: so.Mapped['Book'] = relationship(back_populates='loan')

    user_id: so.Mapped[int] = mapped_column(ForeignKey('users.id'), index=True, primary_key=True)
    user: so.Mapped['User'] = relationship(back_populates='loans')

