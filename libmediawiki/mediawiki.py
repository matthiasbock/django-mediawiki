#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import MySQLdb
from Defines import *

def query(db, cmd, debug=False):
	cursor = db.cursor()
	if debug:
		print q
	cursor.execute(cmd)
	result = cursor.fetchall() 
	if debug:
		print len(result)
	return result

class User:
	def __init__(self, db, q):
		self.database = db
		self.user_id = q[0]
		self.user_name = q[1]
		self.user_real_name = q[2]

class Revision:
	def __init__(self, db, q):
		self.database = db
		self.rev_id = q[0]
		self.rev_page = q[1]
		self.rev_text_id = q[2]
		self.rev_comment = q[3]
		self.rev_user = q[4]

class Page:
	def __init__(self, db, q):
		self.database = db
		self.page_id = q[0]
		self.page_namespace = q[1]
		self.page_title = q[2]

	def getRevisions(self):
		results = []
		for rev in query(self.database, 'SELECT * FROM revision WHERE `rev_page` = '+str(self.page_id)):
			results.append( Revision(self.database, rev) )
		return results

class MediaWiki:
	def __init__(self, host='localhost', port=3306, database='mediawiki', username='guest', password='', debug=True):
		self.database = MySQLdb.connect(host, username, password, database, port=int(port))
		self.database.apilevel = "2.0"
		self.database.threadsafety = 2
		self.database.paramstyle = "format"
		self.debug = debug

	def query(self, q):
		return query(self.database, q, self.debug)

	def getUsers(self):
		results = []
		for user in self.query("SELECT * FROM user"):
			results.append( User(user) )
		return results

	def getPage(self, ID=None, title=None):
		if ID is not None:
			q = self.query("SELECT * FROM page WHERE `page_id` = "+str(ID))
			if len(q) == 1:
				return Page(self.database, q[0])
		elif title is not None:
			q = self.query("SELECT * FROM page WHERE `page_title` = '"+str(title)+"'")
			if len(q) == 1:
				return Page(self.database, q[0])
		return None

	def getPages(self, parent=None, namespace=NS_MAIN):
		results = []
		if parent is None:
			for p in self.query("SELECT * FROM page WHERE `page_namespace` = "+str(namespace)):
				results.append( Page(self.database, p) )
		else:
			for p in self.query("SELECT cl_from FROM categorylinks WHERE `cl_to` = '"+parent.page_title+"'"):
				page = self.getPage( ID=p[0] )
				if str(page.page_namespace) == str(namespace):
					results.append( page )
		return results

