from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

view = Blueprint('projects_view', __name__, template_folder='templates')


@view.route('/projetos')
def home():
    try:
        return render_template("projetos.html")
    except TemplateNotFound:
        abort(404)
