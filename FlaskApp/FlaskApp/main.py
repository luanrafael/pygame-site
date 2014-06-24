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
from models.db_init import init_db
from rest_api import posts_rest_api
from FlaskApp import config
    
app = Flask(__name__)
    
app.config.from_object(config)
init_db()
      
app.register_blueprint(home_views.view)
app.register_blueprint(downloads_views.view)
app.register_blueprint(docs_views.view)
app.register_blueprint(forum_views.view)
app.register_blueprint(projects_views.view)
app.register_blueprint(admin_views.view)
app.register_blueprint(posts_rest_api.posts_api)
    
if __name__ == "__main__":
	app.run(debug=True)
        
        
        
        
        
