from flask import Blueprint, render_template, abort
from flask_login import current_user
from jinja2 import TemplateNotFound

view = Blueprint('downloads_view', __name__, template_folder='templates')


@view.route('/downloads')
def home():

    values = {}
    if current_user:
        values = {"user": current_user}
    return render_template("downloads.html", values=values)
