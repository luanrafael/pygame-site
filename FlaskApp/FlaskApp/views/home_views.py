from flask import Blueprint, render_template
from flask_login import current_user

view = Blueprint('home_view', __name__, template_folder='templates')

@view.route('/')
def home():
    if current_user:
        return render_template("home.html") # TODO usar jinja
    return render_template("home.html")


