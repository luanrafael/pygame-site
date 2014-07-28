# coding: utf-8

from sqlobject import StringCol, DateTimeCol
from model_base import ModelBase

__author__ = 'iury'


class Post(ModelBase):

    """
    Class for store posts
    To create a new Post object just call
     Post(author=author, content=content, title=title)
    you don't need to pass the field date, it is create automatically
    """
    author = StringCol()
    content = StringCol()
    title = StringCol()
    date = DateTimeCol(default=DateTimeCol.now)
    categorie = StringCol(default=None)

    def to_dict(self):
        """
        return a dict of the fields in the class plus the id field,
        which is a unique field for each object
        """
        return {
            'categorie': self.categorie,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date,
            'id': self.id
        }

    @classmethod
    def save_post(cls, author, content, title, categorie):
        post = cls(
            author=author, content=content, title=title, categorie=categorie)
        return post

    @classmethod
    def delete_post(cls, id):
        cls.delete(id)

    @classmethod
    def edit_post(cls, id, dic):
        post = cls.get(id)
        post.author = dic['author']
        post.content = dic['content']
        post.title = dic['title']
        post.categorie = dic['categorie']
