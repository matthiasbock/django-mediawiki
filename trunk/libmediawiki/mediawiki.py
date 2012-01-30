#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import MySQLdb
from Defines import *

class User:
	def __init__(self, q):
		self.user_id = q[0]
		self.user_name = q[1]
		self.user_real_name = q[2]

class Page:
	def __init__(self, q):
		self.page_id = q[0]
		self.page_namespace = q[1]
		self.page_title = q[2]

class Session:
	def __init__(self, host='localhost', port=3306, database='mediawiki', username='guest', password=''):
		self.database = MySQLdb.connect(host, username, password, database, port=int(port))
		self.database.apilevel = "2.0"
		self.database.threadsafety = 2
		self.database.paramstyle = "format"

	def query(self, q):
		cursor = self.database.cursor()
		print q
		cursor.execute(q)
		result = cursor.fetchall() 
		print len(result)
		return result

	def getUsers(self):
		results = []
		for user in self.query("SELECT * FROM user"):
			results.append( User(user) )
		return results

	def getCategories(self, parent):
		results = []
		for p in self.query("SELECT * FROM page WHERE `page_namespace` = "+str(NS_CATEGORY)):
			results.append( Page(p) )
		return results

	def getPages(self, parent):
		return []

