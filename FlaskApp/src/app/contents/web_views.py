# coding: utf-8

from flask import Blueprint, render_template
from flask_login import current_user

web_views = Blueprint('content_web_views', __name__, template_folder='templates')
@web_views.route('/docs')
def docs():
    # values = {}
    # if current_user:
    #     values = {"user": current_user}
    return render_template("docs.html")


@web_views.route('/downloads')
def downloads():
    # values = {}
    # if current_user:
    #     values = {"user": current_user}
    return render_template("downloads.html")

@web_views.route('/forum')
def forum():
    # values = {}
    # if current_user:
    #     values = {"user": current_user}
    return render_template("forum.html")

@web_views.route('/projetos')
def projects():
    # values = {}
    # if current_user:
    #     values = {"user": current_user}
    return render_template("projetos.html")
