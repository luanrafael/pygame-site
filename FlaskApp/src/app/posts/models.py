# coding: utf-8

import datetime
from app import db


class Post(db.Model):

    __tablename__ = "posts"
    session = db.session

    id = db.Column(db.Integer(), primary_key=True)
    author = db.Column(db.Unicode(80))
    content = db.Column(db.UnicodeText())
    title = db.Column(db.Unicode(80))
    date = db.Column(db.DateTime(), onupdate=datetime.datetime.now(), default=datetime.datetime.now)
    categorie = db.Column(db.Unicode(80))

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
            'date': str(self.date),
            'id': self.id
        }

    @classmethod
    def make_commit(cls):
        cls.session.commit()

    @classmethod
    def save(cls, post):
        # TODO: nao deveria
    	# ser classmethod
        cls.session.add(post)
        cls.make_commit()

    @classmethod
    def delete(cls, id):
        # TODO: nao deveria
    	# ser classmethod
        cls.session.query(cls).filter(cls.id == id).delete()
        cls.make_commit()

    @classmethod
    def get_by_id(cls, _id):
        post = cls.session.query(cls).get(_id)
        return post

    @classmethod
    def get_all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def get_from_offset(cls, begin, limit=6):
        return cls.session.query(cls).order_by(cls.id).offset(begin).limit(limit).all()

    @classmethod
    def count(cls):
        return cls.session.query(cls).count()
