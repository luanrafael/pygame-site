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
    _type = StringCol()
    

    @classmethod
    def get_content(cls, _type):
        return Content.selectBy(_type=_type)

    @classmethod
    def save_data(cls, data, _type=""):
        content = Content(data=data, _type=_type)
        return content

    def to_dict(self):
        return{
            "data": self.data,
            "type": self._type
        }
