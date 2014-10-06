#coding: utf-8

import unittest


class PygameTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls, class_name):
		"Name is the name of the model class"

		try:
			class_name.createTable()
		except Exception:
			pass
