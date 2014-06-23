from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('docs_view', __name__, template_folder='templates')


@view.route('/docs')
def home():
    try:
        return render_template("docs.html")
    except TemplateNotFound:
        abort(404)
