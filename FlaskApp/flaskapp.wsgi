#!/usr/bin/python

# use this file to run the webserver inside apache2
# the instalation guide is in the Readme.md
import sys
import logging


logging.basicConfig(stream=sys.stderr)

if '/var/www/FaskApp/FlaskApp' not in sys.path:
    sys.path.insert(0,"/var/www/FlaskApp/FlaskApp")

from FlaskApp.__main__ import app as application

