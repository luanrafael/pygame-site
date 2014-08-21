# coding : utf-8

import os
import hashlib
import random
import sys


def get_secret_key():
	if "pygame_secret_key" not in os.environ:
		return hashlib.sha1(str(random.randint(1, 100))).hexdigest()
	return os.environ["pygame_secret_key"]


def put_project_in_path():
	PROJECT_PATH = os.path.sep.join(
		os.path.abspath(__file__).split(os.path.sep)[:-2]
		)
	if PROJECT_PATH not in sys.path:
		sys.path.append(PROJECT_PATH)
