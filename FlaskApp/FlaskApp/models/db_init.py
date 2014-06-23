#coding: utf-8

# This file includes functions to init and configure the database

from sqlobject import *
from posts import Post

__author__ = 'iury'

def init_db():
    sqlhub.processConnection = connectionForURI("mysql://root:qmagico@localhost/teste")
    Post.createTable(ifNotExists=True)

