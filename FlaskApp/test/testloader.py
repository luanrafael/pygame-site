#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os
import init_test_db

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
ROOT_PATH = os.path.dirname(__file__)

if __name__ == '__main__':
	#find all files which ends with 'tests'

	if PROJECT_PATH not in sys.path:
		sys.path.append(PROJECT_PATH)

	try:
		suite = unittest.TestLoader().discover(sys.argv[1], "*.py")
	except IndexError:
		suite = unittest.TestLoader().discover("test", "*tests.py")

	#initialize the test db    
	cursor = init_test_db.connect_to_database_server()
	init_test_db.create_test_database(cursor, init_test_db.DATABASE_NAME)

    #run tests
	#import pdb; pdb.set_trace()
	result = unittest.TextTestRunner().run(suite)

	if not result.wasSuccessful():
		init_test_db.destroy_test_database(cursor, init_test_db.DATABASE_NAME)
		sys.exit(1)

	init_test_db.destroy_test_database(cursor, init_test_db.DATABASE_NAME)
