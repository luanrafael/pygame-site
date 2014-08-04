# coding: utf-8

from sqlobject import StringCol, BLOBCol
from model_base import ModelBase

__author__ = 'iury'


class Content(ModelBase):

    """
    Class that contains a data of contents
    example: html string data like: <p> hello world! </p>
    """
    data = BLOBCol()
    typeof = StringCol()
    

    @classmethod
    def get_content(cls, _type):
        return Content.selectBy(typeof=_type).limit(1)

    @classmethod
    def get_content_by_id(cls, _id):  # todo: terminar
        return Content.selectBy(id=_id).limit(1)

    @classmethod
    def save_data(cls, _id, data, _type=""):
        content = Content.get_content_by_id(_id)
        if content:
            content.data = data
        return content

    def to_dict(self):
        return{
            "data": self.data,
            "type": self.typeof
        }
