#coding: utf-8

from flask import Blueprint, request, render_template
from FlaskApp.models.user import User
from FlaskApp import db_config
from sqlobject import connectionForURI
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





