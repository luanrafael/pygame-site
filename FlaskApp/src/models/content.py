# coding: utf-8

from sqlobject import StringCol
from model_base import ModelBase

__author__ = 'iury'


class Content(ModelBase):

    """
    Class that contains a data of contents
    example: html string data like: <p> hello world! </p>
    """
    data = StringCol()
    type = StringCol()

    def get_data(type):
        return Content.selectBy(type=type)

    def save_data(data):
        content = Content(data=data)
        return content
