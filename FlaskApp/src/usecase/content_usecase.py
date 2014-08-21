# coding: utf-8

from src.models.content import Content

__author__ = 'iury'


def add_content(data, _type):
    content = get_content(_type)
    if content:
        Content.save_data(content.id, data, _type)


def get_content(_type):
    content = [content for content in Content.get_content(_type)]
    return content[0] if len(content) >= 1 else []
