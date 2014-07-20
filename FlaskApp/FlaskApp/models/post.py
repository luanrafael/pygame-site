#coding: utf-8

from sqlobject import  StringCol, DateTimeCol
from model_base import *

__author__ = 'iury'


class Post(ModelBase):
    """
    Class for store posts
    To create a new Post object just call Post(author=author, content=content, title=title)
    you don't need to pass the field date, it is create automatically
    """
    author = StringCol()
    content = StringCol()
    title = StringCol()
    date = DateTimeCol(default=DateTimeCol.now)
    

    def to_dict(self):
        """
        return a dict of the fields in the class plus the id field, which is a unique field for each object
        """
        return {
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date,
            'id': self.id
        }

    @classmethod
    def save_post(cls, author, content, title):
        post = cls(author=author, content=content, title=title)
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
