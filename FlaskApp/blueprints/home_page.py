from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home_page = Blueprint('home_page', __name__, template_folder='templates')

@home_page.route('/')
def show():
    try:
        return render_template("home.html")
    except TemplateNotFound:
        abort(404)