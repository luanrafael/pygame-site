# coding: utf-8

# This module should  only have operations on
# database level

from app import db


class User(db.Model):

    __tablename__ = 'users'
    session = db.session
    active = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)
    name = db.Column(db.String(80))
    login = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    gender = db.Column(db.String(20))

    def __init__(self, name, login, password, gender, is_admin=False):
        self.name = name
        self.login = login
        self.password = password
        self.gender = gender
        self.is_active = True
        self.is_admin = is_admin

    def to_dict(self):
        return {
            'is_admin': self.admin,
            'is_active': self.active,
            'name': self.name
        }

    def is_active(self):
        return self.is_active

    def is_admin(self):
        return self.is_admin

    @classmethod
    def delete_user(cls, login):
        cls.session.query(cls).filter(cls.login == login).delete()
        cls.session.commit()

    @classmethod
    def get_all_users(cls):
        return cls.session.query(cls).all()

    @classmethod
    def save_user(cls, user):
        cls.session.add(user)
        cls.session.commit()

    @classmethod
    def get_user_by_login(cls, login):
        return cls.session.query(cls).get(login)

    @classmethod
    def get_users(cls):
        return cls.session.query(cls).all()
