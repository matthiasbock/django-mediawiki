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
	def __init__(self, host='localhost', port=3306, database='mediawiki', username='guest', password='', debug=True):
		self.database = MySQLdb.connect(host, username, password, database, port=int(port))
		self.database.apilevel = "2.0"
		self.database.threadsafety = 2
		self.database.paramstyle = "format"
		self.debug = debug

	def query(self, q):
		cursor = self.database.cursor()
		if self.debug:
			print q
		cursor.execute(q)
		result = cursor.fetchall() 
		if self.debug:
			print len(result)
		return result

	def getUsers(self):
		results = []
		for user in self.query("SELECT * FROM user"):
			results.append( User(user) )
		return results

	def getPage(self, ID=None, title=None):
		if ID is not None:
			q = self.query("SELECT * FROM page WHERE `page_id` = "+str(ID))
			if len(q) == 1:
				return Page(q[0])
		elif title is not None:
			q = self.query("SELECT * FROM page WHERE `page_title` = '"+str(title)+"'")
			if len(q) == 1:
				return Page(q[0])
		return None

	def getPages(self, parent=None, namespace=NS_MAIN):
		results = []
		if parent is None:
			for p in self.query("SELECT * FROM page WHERE `page_namespace` = "+str(namespace)):
				results.append( Page(p) )
		else:
			for p in self.query("SELECT cl_from FROM categorylinks WHERE `cl_to` = '"+parent.page_title+"'"):
				page = self.getPage( ID=p[0] )
				if page.page_namespace == str(namespace):
					results.append( page )
		return results

