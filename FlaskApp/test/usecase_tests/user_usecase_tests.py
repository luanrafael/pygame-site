#coding: utf-8

import unittest
import test_base
from sqlobject import SQLObjectNotFound
from src.usecase import user_usecase
from src.models.user import User

class UserTests(test_base.PygameTests):

	@classmethod
	def setUpClass(cls):
		super(UserTests, cls).setUpClass(User)

	def setUp(self):
		user_usecase.delete_all_users()

	def test_add_user(self):

		user_usecase.add_user("iury", "iury",  "passwd", "Male")

		user = user_usecase.get_user_by_login("iury")

		self.assertEqual(user.name,  "iury")
		self.assertEqual(user.login,  "iury")
		self.assertEqual(user.password,  "passwd")
		self.assertEqual(user.gender,  "Male")

	def test_remove_user(self):
		user_usecase.add_user("iury", "iury",  "passwd", "Male")

		user = user_usecase.get_user_by_login("iury")

		user_usecase.delete_user(user.id)

		user = user_usecase.get_user_by_login("iury")

		self.assertIsNone(user)		

