# coding: utf-8

from app.users.models import User


def add_user(name, login, password, gender, is_admin=False):
    user = User(name, login, password, gender, is_admin=is_admin)
    return User.save_user(user)


def delete_user(login):
    return User.delete_user(login)


def delete_all_users():
    for user in User.get_all_users():
        delete_user(user.login)


def get_user_by_login(login):
    return User.get_user_by_login(login)


def check_user_credentials(login, password):
    user = get_user_by_login(login)
    if user is not None:
        if user.password == password:
            return user
    return None

def get_users():
    return User.get_users() or []


def authentic_user(user):
    user.authentic()


def unauthentic_user(user):
    user.unauthentic()
