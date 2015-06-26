# coding: utf-8

import os
from app import app

app.run(host=os.getenv('IP', 'localhost'), port=int(os.getenv('PORT', 5000)))
