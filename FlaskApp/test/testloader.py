#!/usr/bin/env python
# coding: utf-8

import unittest
import sys
import os

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-2])
ROOT_PATH = os.path.dirname(__file__)

sys.stderr = open(os.devnull, 'w')

if __name__ == '__main__':
    try:
        tests = unittest.TestLoader().discover(sys.argv[1], "*tests.py")
    except IndexError:
        tests = unittest.TestLoader().discover(ROOT_PATH, "*tests.py")

    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)
