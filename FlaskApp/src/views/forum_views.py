from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('forum_view', __name__, template_folder='templates')


@view.route('/forum')
def home():
    try:
        return render_template("forum.html")
    except TemplateNotFound:
        abort(404)
