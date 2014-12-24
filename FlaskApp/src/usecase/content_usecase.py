# coding: utf-8

import unittest
from src.models.content import Content

__author__ = 'iury'


def add_content(data, _type):
    Content.save_content(data, _type)


def get_content(_type):
    content = list(Content.get_content(_type))
    return content[0] if content else None


@unittest.skip("typeof should be the primary key of the model")
def delete_content(_type):
    Content.delete_content(_type)


def delete_all_contents():
    for content in Content.select():
        Content.delete(content.id)
