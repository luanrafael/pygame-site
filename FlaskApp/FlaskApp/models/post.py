#coding: utf-8

from sqlobject import  StringCol, DateTimeCol
from model_base import *

class Post(ModelBase):
    author = StringCol()
    content = StringCol()
    title = StringCol()
    date = DateTimeCol(default=DateTimeCol.now)
    

    def to_dict(self):
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
    def edit_post(cls, id, **kwargs):
        post = cls.get(id)

        for key in kwargs:
            if key in post.to_dict():
                setattr(post,key,kwargs[key])
