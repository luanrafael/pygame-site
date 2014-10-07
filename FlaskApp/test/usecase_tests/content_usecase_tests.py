#coding: utf-8

import unittest
import test_base
from sqlobject import SQLObjectNotFound
from src.usecase import content_usecase
from src.models.content import Content


class ContentTests(test_base.PygameTests):

	@classmethod
	def setUpClass(cls):
		super(ContentTests, cls).setUpClass(Content)

	def setUp(self):
		content_usecase.delete_all_contents()

	def test_save_content(self):

		content_data = """
							<p> Olá </p>
							"""
		content_usecase.add_content(content_data, "downloads")

		content = content_usecase.get_content("downloads")

		self.assertEqual(content.data, content_data)


	def test_delete_content(self):
		content_data = """
							<p> Olá </p>
							"""
		content_usecase.add_content(content_data, "downloads")

		content_usecase.delete_content("downloads")

		self.assertEqual(content_usecase.get_content("downloads"), [])



