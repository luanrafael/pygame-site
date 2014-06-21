import os
from flask import Flask
from blueprints.home_page import home_page

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
print template_dir
app = Flask(__name__, template_folder=template_dir)

app.register_blueprint(home_page)

if __name__ == "__main__":
	app.run(debug=True)


