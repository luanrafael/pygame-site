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

cursor = None

def create_test_database():
	global cursor

	logging.info("trying to connect to the database %s" %DATABASE_NAME)
	cursor = MySQLdb.connect(**config_connection)

	logging.info("trying to create the database %s" %DATABASE_NAME)
	cursor.execute("CREATE DATABASE %s" %DATABASE_NAME)

def destroy_test_database():
	global cursor

	logging.info("trying to delete the database: %s" %DATABASE_NAME)
	cursor.execute("DROP DATABASE IF EXISTS %" %DATABASE_NAME)
