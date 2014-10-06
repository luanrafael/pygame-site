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

    def to_dict(self, exclude=None):
        """
        return a dict of the fields in the class plus the id field,
        which is a unique field for each object
        """

        data = {
        		'categorie': self.categorie,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date,
            'id': self.id
            }

        if exclude is not None:
        	for item in exclude:
        		data.pop(item)

        return data

    @classmethod
    def save_post(cls, author, content, title, categorie):
        post = cls(
            author=author, content=content, title=title, categorie=categorie)
        return post

    @classmethod
    def delete_post(cls, id):
        """
        TODO: retornar o status da operacao
        """
        cls.delete(id)

    @classmethod
    def edit_post(cls, id, **kwargs):
        post = cls.get(id)

        if 'author' in kwargs:
        	post.author = kwargs['author']
        if 'content' in kwargs:
        	post.content = kwargs['content']
        if 'title' in kwargs:
        	post.title = kwargs['title']
        if 'categorie' in kwargs:
        	post.categorie = kwargs['categorie']

        return post.id

    @classmethod
    def get_by_id(cls, _id):
    	return cls.selectBy(id=_id)
