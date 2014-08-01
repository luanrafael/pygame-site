# coding: utf-8
		
"""
This file is a helper to create test databases 
"""		
import MySQLdb
import logging

DATABASE_NAME = "test"

# database configuration object
config_connection = {
	"host": "localhost",
	"user": "root",
	"passwd": "pygame"
}


def connect_to_database_server():
	"""
	Connect to a database server, 
	using the config_connection dict
	:Return: a cursor to the connection or None
	"""
	logging.info("trying to connect to the server")
	cursor = MySQLdb.connect(**config_connection).cursor()
	return cursor

def create_test_database(cursor, name):
	"""
	Create a test database with the connection 
	represented by cursor and name represented by
	name. If the database already exists  then 
	the database is deleted and created again
	"""
	
	logging.info("trying to create the database %s" %name)
	try:
		cursor.execute("CREATE DATABASE %s" %name)
	except ProgrammingError:
		logging.info("database %s exists!" %name)
		destroy_test_database(name)
		cursor.execute("CREATE DATABASE %s" %name)

def destroy_test_database(cursor, name):
	"""
	Destroy the test database if the 
	database exists
	"""
	logging.info("trying to delete the database: %s" %name)
	cursor.execute("DROP DATABASE IF EXISTS %" %name)


if __name__ == '__main__':
	cursor = connect_to_database(DATABASE_NAME)
	if cursor is not None:
		create_test_database(cursor, DATABASE_NAME)