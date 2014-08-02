#coding: utf-8

from src.models.post import Post

__author__ = 'iury'



def get_all_posts():
    """
    Return all posts
    """
    return Post.select()

def get_post_by_id(id):
    """
    Get a post by an id 
    """
    return Post.selectBy() #TODO: terminar

def save_post(author, content, title, subject):
    """
    Save a post and return the id of
    the saved post
    """
    post = Post.save_post(author, content, title, subject)
    return post.id

def delete_post(id):
    """
    Delete a post by id
    """
    has_success_on_delete = Post.delete_post(id)
    return has_success_on_delete

def edit_post(id, **kwargs):
    """
    Edit a post
    kwargs is the attributes to edit
    return the id od the post
    """
    post = Post.edit_post(id, kwargs)
    return post.id
