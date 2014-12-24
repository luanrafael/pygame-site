# coding: utf-8

from app import db

class Content(db.Model):

    __tablename__ = "contents"
    session = db.session
    data = db.Column(db.Text())
    _type = db.Column(db.String(80), primary_key=True)

    def __init__(self, data, type):
        self.data = data
        self._type = type

    def to_dict(self):
        return{
            "data": self.data,
            "_type": self._type,
        }

    @classmethod
    def make_commit(cls):
        cls.session.commit()

    @classmethod
    def get_contents(cls):
        return cls.session.query(cls).all()

    @classmethod
    def get_content_by_type(cls, _type):
        return cls.session.query(cls).get(_type)

    @classmethod
    def save_content(cls, content):
        cls.session.add(content)
        cls.make_commit()

        return content._type

    @classmethod
    def delete_content(cls, _type):
        cls.session.query(cls).filter(cls._type == _type).delete()
        cls.make_commit()
