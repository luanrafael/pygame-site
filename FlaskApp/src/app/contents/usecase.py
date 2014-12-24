# coding: utf-8

from models import Content

def delete_all_contents():
    for content in get_contents():
        delete_content(content._type)

def get_contents():
    return Content.get_contents()

def delete_content(_type):
    return Content.delete_content(_type)

def add_content(data, _type):
    content = Content(data, _type)

    return Content.save_content(content)

def edit_content(_type, **kwargs):
    data = kwargs.get("data")

    content = Content.get_content_by_type(_type)

    if content is None:
        return None

    if data is not None:
        content.data = data

    Content.make_commit()
    return content
