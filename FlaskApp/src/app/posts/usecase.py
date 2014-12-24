# coding: utf-8

from models import Post

def get_posts(quantity=None):
    return Post.get_posts(quantity=quantity)

def delete_all_posts():
    for post in get_posts():
        delete_post(post.id)

def delete_post(id):
    Post.delete_post(id)

def add_post(author, content, title, categorie):
    post = Post(author, content, title, categorie)
    Post.save_post(post)
    return post.id

def edit_post(id, **kwargs):
    author = kwargs.get("author")
    content = kwargs.get("content")
    title = kwargs.get("title")
    categorie = kwargs.get("categorie")

    post = Post.get_by_id(id)
    if post is None:
        return None
    if author is not None:
        post.author = author
    if content is not None:
        post.content = content
    if title is not None:
        post.title = title
    if categorie is not None:
        post.categorie = categorie
    Post.make_commit()

    return post