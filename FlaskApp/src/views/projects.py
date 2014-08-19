from flask import Blueprint, render_template
from flask_login import current_user

view = Blueprint('projects_view', __name__, template_folder='templates')


@view.route('/projetos')
def home():
    values = {}
    if current_user:
        values = {"user": current_user}
    return render_template("projetos.html", values=values)
