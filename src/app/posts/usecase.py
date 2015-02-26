# coding: utf-8

from models import Post


def count_posts():
    return Post.count()


def get_posts(begin):
    return Post.get_from_offset(begin)


def delete_all_posts():
    """This is a slow operation  if you have
    many posts
    """
    for post in Post.get_all():
        delete_post(post.id)


def delete_post(id):
    Post.delete(id)


def add_post(author, content, title, categorie):
    post = Post(author, content, title, categorie)
    Post.save(post)
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
