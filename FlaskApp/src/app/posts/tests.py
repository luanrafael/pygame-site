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

from app.posts import usecase as post_usecase
import app

class PostsApiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.db.create_all()

    @classmethod
    def tearDownClass(cls):
        app.db.drop_all()

    def setUp(self):
        self.client = app.Flask.test_client(app.app)
        self.maxDiff = None

    def tearDown(self):
        post_usecase.delete_all_posts()

    def test_get_post(self):
        post_usecase.add_post("iury", "teste", "teste", "pygame")

        data = json.dumps({"quantity": 1}) # because we just have one =(
        response = self.client.get("/api/posts/get", data=data)

        data = json.loads(response.data)
        post = data["data"][0]
        post.pop("id")
        post.pop("date")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(post, {
            u'categorie': u'pygame',
            u'title': u'teste',
            u'author': u'iury',
            u'content': u'teste'
        })

    def test_delete_post(self):
        post_id = post_usecase.add_post("iury", "teste", "teste", "pygame")

        data = json.dumps({"id": post_id})
        response = self.client.post("/api/posts/delete", data=data)

        self.assertEqual(response.status_code, 200)

    def test_edit_post(self):
        post_id = post_usecase.add_post("iury", "teste", "teste", "pygame")

        data = json.dumps({"id": post_id, "title": "new title", "content": "new content"})

        response = self.client.post("/api/posts/edit",data=data)

        data = json.loads(response.data)
        post = data["data"]
        post.pop("id")
        post.pop("date")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(post, {
            u'author': u'iury',
            u'categorie': u'pygame',
            u'content': u'new content',
            u'title': u'new title'
        })

    def test_add_post(self):
        data = json.dumps({"title": "new post", "author": "me", "content": "<p> hello </p>", "categorie": "pygame"})

        response = self.client.post("/api/posts/add", data=data)

        self.assertEqual(response.status_code, 200)

    def test_edit_post_that_doesnt_exists(self):
        data = json.dumps({"id": 42, "title": "new title", "content": "new content"})

        response = self.client.post("/api/posts/edit", data=data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, "post object does not exists")