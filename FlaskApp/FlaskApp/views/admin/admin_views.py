#coding: utf-8

from flask import Blueprint, render_template
from flask_login import login_required

view = Blueprint('admin_view', __name__, template_folder='templates')


@view.route('/admin')
@login_required
def home():
    return render_template("admin.html")



