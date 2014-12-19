# coding: utf-8

from src.models.post import Post

__author__ = 'iury'

def get_all_posts():
    """
    Return all posts
    """
    return [post for post in Post.select().orderBy('date')]


def save_post(author, content, title, categorie):
    """
    Save a post and return the id of
    the saved post
    """
    post = Post.save_post(author, content, title, categorie)
    return post.id


def delete_post(_id):
    """
    Delete a post by id
    """
    return Post.delete_post(_id)


def edit_post(_id, dic):
    """
    Edit a post
    kwargs is the attributes to edit
    return the id od the post
    """
    _id = Post.edit_post(_id, **dic)
    return _id

def delete_all_posts():
	for post in Post.select():
		delete_post(post.id)
