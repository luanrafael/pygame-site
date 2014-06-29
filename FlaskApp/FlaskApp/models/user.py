#coding: utf-8

from sqlobject import BoolCol, StringCol
from model_base import ModelBase

__author__ = 'iury'

class User(ModelBase):
    is_active = BoolCol()
    is_admin = BoolCol()
    name = StringCol()
    login = StringCol()
    password = StringCol()
    gender = StringCol()

    def to_dict(self):
        return{
            'is_admin': self.is_admin,
            'is_active': self.is_active,
            'name': self.name
        }

    def is_active(self):
        return self.is_active

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


    def is_admin(self):
        return self.is_admin

    @classmethod
    def get_all_users(cls):
        return User.select()

    @classmethod
    def get_user(cls, id):
        return User.get(id)

    @classmethod
    def get_user_by_login_n_password(cls, login, password):
        return User.selectBy(login=login, password=password)