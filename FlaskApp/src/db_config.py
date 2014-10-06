# coding: utf-8

# This file includes functions to init and configure the database

import logging
from sqlobject import sqlhub, connectionForURI
import MySQLdb

def get_database_uri(schema, user, passswd, database):
	return "%s://%s:%s@localhost/%s" %(schema, user, passswd, database)
	
def connect_to_database(user, passwd, host="localhost"):
	return MySQLdb.connect(**locals())

def create_database(cursor, name):
	try:
		cursor.execute("CREATE DATABASE %s" %name)
	except MySQLdb.ProgrammingError:
		logging.warning("database already exists!")

def delete_database(cursor, name):
	cursor.execute("DROP DATABASE %s" %name)

def init_db(database_uri):
  sqlhub.processConnection = connectionForURI(database_uri)
