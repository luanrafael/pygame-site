from utils import *

put_project_in_path()

from flask import Flask
from flask_login import LoginManager
from views import home_views, downloads_views, login
from views import docs_views
from views import forum_views
from views import projects_views
from views import admin_views
from rest_api import posts_rest_api, contents_rest_api
from src import config
from db_config import init_db
from src.models.user import User

# Configuring the application

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = get_secret_key()
init_db()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

blueprints = [
    home_views.view, downloads_views.view, docs_views.view,
    forum_views.view, projects_views.view,
    admin_views.view, posts_rest_api.posts_api, login.view,
    contents_rest_api.contents_api
]

map(app.register_blueprint, blueprints)

if __name__ == "__main__":
	app.run(debug=config.debug)
