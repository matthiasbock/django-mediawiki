#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import MySQLdb

from user import User

class Session:
	def __init__(self, host='localhost', port=3306, database=None, username=None, password=None):
		self.database = MySQLdb.connect(host, user, password, db)
		self.database.apilevel = "2.0"
		self.database.threadsafety = 2
		self.database.paramstyle = "format"

	def query(self, q):
		cursor = self.database.cursor()
		cursor.execute(q)
		return cursor.fetchall() 

	def getUsers(self):
		results = []
		for user in self.database.user.SELECT():
			results.append( User(user) )
		return results

	def getCategories(parent):
		return[]

	def getPages(parent):
		return []

