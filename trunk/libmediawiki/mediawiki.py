#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from database import Database
from user import User

class Session:
	def __init__(self, host='localhost', port=3306, database=None, username=None, password=None):
		self.database = Database()
		self.database.connect(host, port)
		self.database.login(username, password)
		self.database.open(database)

	def getusers(self):
		results = []
		for user in self.database.user.all():
			results.append( User(user) )
		return results

