# coding: utf-8

from flask import Blueprint, render_template, redirect, request, session
from flask_login import current_user, login_user
import usecase

web_views = Blueprint('user_web_views', __name__, template_folder='templates')


@web_views.route('/admin')
def admin():
    values = {}
    if not current_user.is_authenticated:
        return redirect('/login')

    values["user"] = current_user.name
    return render_template("admin.html")


@web_views.route('/signup', methods=["POST"])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    gender = None
    if request.form.get("male"):
        gender = 'male'
    if request.form.get("female"):
        gender = 'female'

    if all([name, email, password, gender]):
        user = usecase.add_user(name, email,  password, gender, is_admin=True)
        login_user(user)
        return redirect('/admin')
    return redirect('/login')

@web_views.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        password = request.form.get("password")
        login = request.form.get("login")

        user = usecase.check_user_credentials(login, password)
        if user is not None:
            usecase.authentic_user(user)
            login_user(user)
            return redirect('/admin')
        else:
            return "usuario  inexistente"

    return render_template('sign-in-up.html')


@web_views.route("/logout", methods=["GET"])
def logout():
    #logout_user()
    return redirect('/')


