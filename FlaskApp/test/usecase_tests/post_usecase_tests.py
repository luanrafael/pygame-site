#coding utf-8

import unittest
from mock import Mock
from src.usecase import posts

class PostTests(unittest.TestCase):

	def setUp(self):
		super(PostTests, self).setUp()
		self.mock = Mock(posts)

	def test_get_all_posts(self):
		
		self.assertTrue(posts)
		self.assertEquals(post, posts[0])