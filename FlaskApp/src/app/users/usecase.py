#coding: utf-8

from app.users.models import User
from app import db

def add_user(name, login, password, gender):
	user = User(name, login, password, gender)
	User.save_user(user, db.session)

def delete_user(id):
	return User.delete_user(id)

def delete_all_users():
	for user in User.get_all_users():
		delete_user(user.id)

def get_user_by_login(login):
	return User.get_user_by_login(login)
