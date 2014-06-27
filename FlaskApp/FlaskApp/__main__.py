import sys, os

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
if PROJECT_PATH not in sys.path:
    sys.path.insert(0,PROJECT_PATH)
    
from flask import Flask
from views import home_views, downloads_views
from views.docs import docs_views
from views.forum import forum_views
from views.projects import projects_views
from views.admin import admin_views
from rest_api import posts_rest_api
from FlaskApp import config
from db_config import init_db

app = Flask(__name__)
app.config.from_object(config)
init_db()

blueprints = {home_views.view, downloads_views.view, docs_views.view, forum_views.view, projects_views.view,
              admin_views.view, posts_rest_api.posts_api}

map(app.register_blueprint, blueprints)

if __name__ == "__main__":
	app.run(debug=True)
        
        
        
        
        
