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
    type = StringCol()
    

    def get_content(type):
        return Content.selectBy(type=type)

    @classmethod
    def save_data(cls, data, _type=""):
        content = Content(data=data, type=_type)
        return content
