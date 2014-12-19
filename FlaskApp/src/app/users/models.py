# coding: utf-8

__author__ = 'iury'

from app import db

class User(db.Model):

		__tablename__ = 'users'
		active = db.Column(db.Boolean)
		admin = db.Column(db.Boolean)
		name = db.Column(db.String(80))
		login = db.Column(db.String(80), primary_key=True)
		password = db.Column(db.String(80))
		gender = db.Column(db.String(20))

		def __init__(self, name, login, password, gender):
			self.name = name
			self.login = login
			self.password = password
			self.gender = gender

		def to_dict(self):
			return{
            'is_admin': self.admin,
            'is_active': self.active,
            'name': self.name
        }

		def is_active(self):
			return True

		def is_authenticated(self):
			return True

		def is_anonymous(self):
			return False

		def get_id(self):
			return self.id

		def is_admin(self):
			return self.admin

		@classmethod
		def delete_user(cls, id):
			cls.delete(id)

		@classmethod
		def get_all_users(cls):
			return cls.query.all()

		@classmethod
		def save_user(cls, user, session):
			session.add(user)
			session.commit()

		@classmethod
		def get_user_by_login(cls, login):
			return cls.query(login=login).first()
