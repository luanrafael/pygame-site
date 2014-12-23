# coding: utf-8

import os
import sys
import unittest
import json

PROJECT_PATH = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-3]
)
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from app.users import usecase as user_usecase
import app


class UserApiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.db.create_all()

    def setUp(self):
        self.client = app.Flask.test_client(app.app)
        user_usecase.delete_all_users()

    def test_get_by_login(self):
        user_usecase.add_user("iury", "iury", "passwd", "Male")
        data  = json.dumps({"login": "iury"})
        response = self.client.post("/api/users/get_by_login", data=data)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {u'is_active': None, u'is_admin': None, u'name': u'iury'})

    def test_add_user(self):

        data  = json.dumps({"login": "iury", "name": "iury", "password": "passwd", "gender": "Male"})
        response = self.client.post("/api/users/add", data=data)
        self.assertEqual(response.status_code, 200)

    def test_remove_user(self):
        user_usecase.add_user("iury", "iury", "passwd", "Male")
        data  = json.dumps({"login": "iury"})
        response = self.client.post("/api/users/delete", data=data)

        self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        user_usecase.add_user("iury", "iury", "passwd", "Male")
        response = self.client.get("/api/users/get_all")
        json_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data["data"], [{u'is_admin': None, u'is_active': None, u'name': u'iury'}])

if __name__ == '__main__':
    unittest.main()
