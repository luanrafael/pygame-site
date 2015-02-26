# coding: utf-8

from flask import Blueprint, render_template

web_views = Blueprint('post_web_views', __name__, template_folder='templates')


@web_views.route("/")
def home():
    return render_template("home.html")
