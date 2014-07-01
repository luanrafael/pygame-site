#coding: utf-8

from flask_login import login_user
from flask import Blueprint, request, render_template
from FlaskApp.models.user import User
__author__ = 'iury'

view = Blueprint('login', __name__)

@view.route('/login', methods=["GET", "POST"])
def login():
    if len(request.form) == 0:
        return render_template('sign-in-up.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = User.get_user_by_login_n_password(username, password)

@view.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form['name']
    password = request.form['password']
    email = request.form['email']
    gender = request.form['gender']

    user = User(name=username, login=email, password=password, gender=gender)
    login_user(user)
    return render_template('home.html')