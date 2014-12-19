from utils import get_secret_key, put_project_in_path

put_project_in_path()

from flask import Flask
from flask_login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from views import (home, downloads, login, docs, forum, projects, admin)
from rest_api import posts_rest_api, contents_rest_api
from src import config
import db_config
from src.models.user import User

# Configuring the application

app = Flask(__name__)
app.config.from_object(config)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:pygame@localhost/test2"
db = SQLAlchemy(app)
app.secret_key = get_secret_key()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

blueprints = [
    home.view, downloads.view, docs.view, forum.view, projects.view,
    admin.view, posts_rest_api.posts_api, login.view,
    contents_rest_api.contents_api,
]

map(app.register_blueprint, blueprints)

if __name__ == "__main__":
	app.run(debug=config.debug)
