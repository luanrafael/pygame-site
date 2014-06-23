from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('downloads_view', __name__, template_folder='templates')

@view.route('/downloads')
def home():
    try:
        return render_template("downloads.html")
    except TemplateNotFound:
        abort(404)

