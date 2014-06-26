#coding: utf-8

from sqlobject import  StringCol, DateTimeCol, IntCol
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