#coding: utf-8

from src.models.content import Content

__author__ = 'iury'


def add_content(content, _type):
	Content.save_data(content, _type)
