# coding: utf-8

from sqlobject import StringCol, BLOBCol
from model_base import ModelBase


class Content(ModelBase):

    """
    Class that contains a data of contents
    example: html string data like: <p> hello world! </p>
    """
    data = BLOBCol()
    typeof = StringCol()

    @classmethod
    def get_content(cls, _type):
        return cls.selectBy(typeof=_type).limit(1)

    @classmethod
    def get_content_by_id(cls, _id):  # todo: terminar
        return Content.selectBy(id=_id).limit(1)

    @classmethod
    def save_content(cls, data, _type=""):
    		content = cls(data=data, typeof=_type)

    		return content.id

    @classmethod
    def delete_content(cls, _id):
    	cls.delete(_id)

    def to_dict(self):
        return{
            "data": self.data,
            "type": self.typeof
        }
