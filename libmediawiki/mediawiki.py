#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import MySQLdb
from Defines import *

def query(db, cmd, debug=False):
	cursor = db.cursor()
	if debug:
		print cmd
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

class Text:
	def __init__(self, db, q):
		self.database = db
		self.old_id = q[0]
		self.old_text = q[1]

	def __str__(self):
		return self.old_text

class Revision:
	def __init__(self, db, q):
		self.database = db
		self.rev_id = q[0]
		self.rev_page = q[1]
		self.rev_text_id = q[2]
		self.rev_comment = q[3]
		self.rev_user = q[4]
		self.rev_timestamp = q[6]
		self.rev_minor_edit = str(q[7]) == '1'

	def getText(self):
		q = query(self.database, 'SELECT * FROM text WHERE `old_id` = '+str(self.rev_text_id))
		if len(q) == 1:
			return Text( self.database, q[0] )
		return None

class Page:
	def __init__(self, db, q):
		self.database = db
		self.page_id = q[0]
		self.page_namespace = q[1]
		self.page_title = q[2]
		self.page_counter = q[4]
		self.page_is_redirect = str(q[5]) == '1'
		self.page_latest = q[9]

	def getRevisions(self):
		results = []
		for rev in query(self.database, 'SELECT * FROM revision WHERE `rev_page` = '+str(self.page_id)):
			results.append( Revision(self.database, rev) )
		return results

	def getText(self):
		q = query(self.database, 'SELECT * FROM text WHERE `old_id` = '+str(self.page_latest))
		if len(q) == 1:
			return Text( self.database, q[0] )
		return None

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
			results.append( User(self.database, user) )
		return results

	def getPage(self, ID=None, title=None, namespace=None):

		query = "SELECT * FROM page WHERE "
		AND = False

		if ID is not None:
			query += "`page_id` = "+str(ID)+" "
			AND = True

		if title is not None:
			if AND:
				query += "AND "
			query += "`page_title` = '"+str(title)+"'"
			AND = True

		if namespace is not None:
			if AND:
				query += "AND "
			query += "`page_namespace` = "+str(namespace)

		result = self.query(query)
		if len(result) == 1:
			return Page(self.database, result[0])
		return None

	def getPages(self, parent=None, namespace=None):
		results = []
		if parent is None:
			q = "SELECT * FROM page"
			if namespace is not None:
				q += " WHERE `page_namespace` = "+str(namespace)
			for p in self.query(q):
				results.append( Page(self.database, p) )
		else:
			for p in self.query("SELECT cl_from FROM categorylinks WHERE `cl_to` = '"+parent.page_title+"'"):
				page = self.getPage( ID=p[0] )
				if (namespace is None or str(page.page_namespace) == str(namespace)) and page is not None:
					results.append( page )
				else:
					del page
		return results

