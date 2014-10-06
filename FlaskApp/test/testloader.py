#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os



if __name__ == '__main__':
	
	PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])

	#put the project in path
	if PROJECT_PATH not in sys.path:
		sys.path.append(PROJECT_PATH)

	from  src import db_config

	cursor = db_config.connect_to_database("root", "pygame").cursor()
	db_config.create_database(cursor, "test2")
	uri = db_config.get_database_uri("mysql", "root", "pygame", "test2")
	db_config.init_db(uri)
	#find all files which ends with 'tests'
	suite = unittest.TestLoader().discover(".", "*.py")
  #run tests
	result = unittest.TextTestRunner().run(suite)

	if not result.wasSuccessful():
		db_config.delete_database(cursor, "test2")
		sys.exit(1)

	db_config.delete_database(cursor, "test2")
