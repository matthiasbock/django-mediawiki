#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import MySQLdb

class User:
	def __init__(self, q):
		self.user_id = q[0]
		self.user_name = q[1]
		self.user_real_name = q[2]

class Session:
	def __init__(self, host='localhost', port=3306, database=None, username=None, password=None):
		self.database = MySQLdb.connect(host, username, password, database, port=int(port))
		self.database.apilevel = "2.0"
		self.database.threadsafety = 2
		self.database.paramstyle = "format"

	def query(self, q):
		cursor = self.database.cursor()
		cursor.execute(q)
		return cursor.fetchall() 

	def getUsers(self):
		results = []
		for user in self.query("SELECT * FROM user"):
			results.append( User(user) )
		return results

	def getCategories(self, parent):
		return[]

	def getPages(self, parent):
		return []

