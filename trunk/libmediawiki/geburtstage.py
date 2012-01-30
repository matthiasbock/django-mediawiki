#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from mediawiki import *
from ConfigParser import RawConfigParser

parser = RawConfigParser()
parser.read('test.conf')
host	= parser.get('test', 'host')
port	= parser.get('test', 'port')
db	= parser.get('test', 'database')
user	= parser.get('test', 'username')
pw	= parser.get('test', 'password')

wiki = MediaWiki(host, port, db, user, pw, debug=False)

for page in wiki.getPages( parent=wiki.getPage(title='Geburtstage') ):
	for line in str(page.getText()).split('\n'):
		if line.find('{{Geburtstag') > -1:
			print page.page_title+': '+line

