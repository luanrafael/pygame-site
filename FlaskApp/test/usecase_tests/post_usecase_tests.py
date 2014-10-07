#coding utf-8

import unittest
import test_base
from sqlobject import SQLObjectNotFound
from src.usecase import posts_usecase
from src.models.post import Post


class PostTests(test_base.PygameTests):

	@classmethod
	def setUpClass(cls):
		super(PostTests, cls).setUpClass(Post)
		
	def setUp(self):

		#common data for all tests in this class
		self.post_data = {
			"author": "me",
			"content": "content",
			"title": "title",
			"categorie": "subject"
		}

	def test_get_all_posts(self):
		posts_usecase.delete_all_posts()
		posts = [post for post in posts_usecase.get_all_posts()]

		#we don't have posts =(
		self.assertEquals(posts, [])
		#adding a post
		posts_usecase.save_post(
			self.post_data["author"], self.post_data["content"], self.post_data["title"],
			self.post_data["categorie"]
			)

		posts = [post.to_dict(exclude=["date", "id"]) for post in posts_usecase.get_all_posts()]

		# we must have one post
		self.assertEquals(len(posts), 1)
		self.assertEquals(posts, [self.post_data])

	def test_save_post(self):
		#adding a post
		saved_post_id = posts_usecase.save_post(
			self.post_data["author"], self.post_data["content"], self.post_data["title"],
			self.post_data["categorie"]
			)

		post = list(Post.get_by_id(saved_post_id))
		# the saved_post should have this values

		self.assertEquals(post[0].to_dict(exclude=["id", "date"]), self.post_data)

	def test_try_delete_post(self):
		#adding a post
		saved_post = posts_usecase.save_post(
			self.post_data["author"], self.post_data["content"], self.post_data["title"], 
			self.post_data["categorie"]
		)

		posts_usecase.delete_post(saved_post)
		_id = Post.get_by_id(saved_post)
		self.assertEquals(list(_id), [])

	def test_try_delete_post_that_dont_exists(self):

		with self.assertRaises(SQLObjectNotFound):
			posts_usecase.delete_post(10)

	def test_edit_post(self):

	 	#adding a post 
		_id = posts_usecase.save_post(
			self.post_data["author"], self.post_data["content"], self.post_data["title"], 
			self.post_data["categorie"]
	  	)

	 	# modify the subject of the post
	 	content = "hey what's up"

	 	# save the post with another subject
	 	post_id = posts_usecase.edit_post(_id, {"content": content})

	 	# get the post with id = post_id
	 	post = list(Post.get_by_id(post_id))[0]

	 	# the subject must be are modified subject
	 	self.assertEquals(content, post.content)
