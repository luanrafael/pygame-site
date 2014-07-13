#coding: utf-8

from flask import Blueprint, render_template
from flask_login import current_user

view = Blueprint('admin_view', __name__, template_folder='templates')


@view.route('/admin')
def home():

    if not current_user.is_authenticated():
        return 'Voce não tem permissão para acessar essa página'
    return render_template("admin.html")



