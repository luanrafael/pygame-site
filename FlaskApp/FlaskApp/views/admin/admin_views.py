from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('admin_view', __name__, template_folder='templates')

@view.route('/admin')
def home():
    return render_template("login.html")

