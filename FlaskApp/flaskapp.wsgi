#!/usr/bin/python

# use this file to run the webserver inside apache2
# the instalation guide is in the Readme.md
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application

