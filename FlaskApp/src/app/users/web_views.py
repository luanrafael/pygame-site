# coding: utf-8

from flask import Blueprint, render_template, redirect
from flask_login import current_user

web_views = Blueprint('user_web_views', __name__, template_folder='templates')


@web_views.route('/admin')
def admin():
    # TODO: consertar
    # values = {}
    # if not current_user.is_authenticated():
    #     return 'Voce não tem permissão para acessar essa página'

    # values["user"] = current_user.name
    return render_template("admin.html")


@web_views.route('/login', methods=["GET"])
def login():
    return render_template('sign-in-up.html')


@web_views.route("/logout", methods=["GET"])
def logout():
    #logout_user()
    return redirect('/')


