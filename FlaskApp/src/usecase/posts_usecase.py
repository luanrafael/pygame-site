# coding: utf-8

from src.models.post import Post

__author__ = 'iury'


def get_all_posts():
    """
    Return all posts
    """
    posts = []
    _max = 0
    ind = 1
    for post in Post.select().orderBy('date'):
        post_dict = post.to_dict()
        post_dict['ind'] = ind
        _max += 1

        posts.append(post_dict)
        if _max == 5:
            _max = 0
            ind += 1
    return posts


def get_post_by_id(id):
    """
    Get a post by an id
    """
    return Post.selectBy()  # TODO: terminar


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
    has_success_on_delete = Post.delete_post(_id)
    return has_success_on_delete


def edit_post(_id, dic):
    """
    Edit a post
    kwargs is the attributes to edit
    return the id od the post
    """
    _id = Post.edit_post(_id, **dic)
    return _id
