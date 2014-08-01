#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os
import init_test_db

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
ROOT_PATH = os.path.dirname(__file__)
sys.stderr = open(os.devnull, 'w')

if __name__ == '__main__':

	#find all files which ends with 'tests'
    try:
        tests = unittest.TestLoader().discover(sys.argv[1], "*tests.py")
    except IndexError:
        tests = unittest.TestLoader().discover(ROOT_PATH, "*tests.py")

    #initialize the test db    
    cursor = init_test_db.connect_to_database_server()
    init_test_db.create_test_database(cursor, init_test_db.DATABASE_NAME)

    #run tests
    result = unittest.TextTestRunner().run(tests)
    if not result.wasSuccessful():
        sys.exit(1)
        init_test_db.destroy_test_database(cursor, init_test_db.DATABASE_NAME)
    else:
    	init_test_db.destroy_test_database(cursor, init_test_db.DATABASE_NAME)
