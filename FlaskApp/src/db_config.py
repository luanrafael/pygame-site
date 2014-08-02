# coding: utf-8

# This file includes functions to init and configure the database

from sqlobject import sqlhub, connectionForURI

__author__ = 'iury'

schema = "mysql"
database = "teste"
user = "root"
password = "pygame"
database_uri = schema + "://" + user + \
    ":" + password + "@localhost/" + database


def init_db():
    sqlhub.processConnection = connectionForURI(database_uri)
