#coding utf-8

import unittest
from src.usecase import posts_usecase

class PostTests(unittest.TestCase):

	def setUp(self):
		super(PostTests, self).setUp()
		#common data for all tests in that class
		self.post_data = {
			"author": "me",
			"content": "content",
			"title": "title",
			"subject": "subject"
		}

	def get_all_posts_test(self):

		posts = [post for post in posts_usecase.get_all_posts()]

		#we don't have posts =(
		self.assertEquals(posts, [])

		#adding a post
		posts_usecase.save_post(
			self.post_data["me"], self.post_data["content"], self.post_data["title"], 
			self.post_data["subject"]
			)

		posts = [post for post in posts_usecase.get_all_posts()]

		# we must have one post
		self.assertEquals(len(posts), 1)

	def save_post_test(self):

		#adding a post
		saved_post = posts_usecase.save_post(
			self.post_data["me"], self.post_data["content"], self.post_data["title"], 
			self.post_data["subject"]
			)

		# id must be a atrr of saved_post
		self.assertTrue('id' in post.__dict__)

		# the saved_post should have this values
		self.assertEquals(saved_post.to_dict(), self.post_data)


	def try_delete_post_test(self):

		#adding a post
		saved_post = posts_usecase.save_post(
			self.post_data["me"], self.post_data["content"], self.post_data["title"], 
			self.post_data["subject"]
			)		
		
		# should return true if the post was successfull removed
		delete_status = posts_usecase.delete_post(save_post.id) 
		self.assertTrue(delete_status)

	def try_delete_post_that_dont_exists_test(self):

		# should return false, because the post with this id does not exist
		self.assertFalse(posts_usecase.delete_post(10))


	def edit_post_test(self):

		#adding a post 
		saved_post = posts_usecase.save_post(
			self.post_data["me"], self.post_data["content"], self.post_data["title"], 
			self.post_data["subject"]
			)		

		# modify the subject of the post
		saved_post['subject'] = "hey what's up"

		# save the post with another subject
		post_id = posts_usecase.edit_post(saved_post["subject"])

		# get the post with id = post_id
		post = posts_usecase.get_post_by_id(post_id)

		# the subject must be are modified subject
		self.assertEquals(saved_post["subject"], post.subject)