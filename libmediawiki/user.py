#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

class User:
	def __init__(self, query_result):
		self.__dict__.update(query_result)
		return self
