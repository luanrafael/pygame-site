# coding: utf-8

import os
import sys
import unittest

PROJECT_PATH = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-3]
)
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from app.users import usecase as user_usecase
import app


class UserTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.db.create_all()

    def setUp(self):
        user_usecase.delete_all_users()

    def test_add_user(self):

        user_usecase.add_user("iury", "iury", "passwd", "Male", is_admin=True)

        user = user_usecase.get_user_by_login("iury")

        self.assertEqual(user.name, "iury")
        self.assertEqual(user.login, "iury")
        self.assertEqual(user.password, "passwd")
        self.assertEqual(user.gender, "Male")

    def test_remove_user(self):
        user_usecase.add_user("iury", "iury", "passwd", "Male")

        user = user_usecase.get_user_by_login("iury")

        user_usecase.delete_user(user.login)

        user = user_usecase.get_user_by_login("iury")

        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
