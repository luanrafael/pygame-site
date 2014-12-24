# coding: utf-8

import datetime
from app import db


class Post(db.Model):

    __tablename__ = "posts"
    session = db.session

    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.String(80))
    content = db.Column(db.Text())
    title = db.Column(db.String(80))
    date = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    categorie = db.Column(db.String(80))

    def __init__(self, author, content, title, categorie):
        self.author = author
        self.content = content
        self.title = title
        self.categorie = categorie

    def to_dict(self):
        return {
        	'categorie': self.categorie,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date,
            'id': self.id
            }

    @classmethod
    def make_commit(cls):
        cls.session.commit()

    @classmethod
    def save_post(cls, post):
        cls.session.add(post)
        cls.make_commit()

    @classmethod
    def delete_post(cls, id):
        cls.session.query(cls).filter(cls.id == id).delete()
        cls.make_commit()

    @classmethod
    def get_by_id(cls, _id):
        post = cls.session.query(cls).get(_id)
        return post

    @classmethod
    def get_posts(cls, quantity=None):
        if quantity is not None:
            return cls.session.query(cls).order_by(cls.id).limit(quantity).all()
        return cls.session.query(cls).all()