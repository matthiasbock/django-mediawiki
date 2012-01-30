#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import mediawiki
from ConfigParser import RawConfigParser

parser = RawConfigParser()
parser.read('test.conf')
host	= parser.get('test', 'host')
port	= parser.get('test', 'port')
db	= parser.get('test', 'database')
user	= parser.get('test', 'username')
pw	= parser.get('test', 'password')

session = mediawiki.Session(host, port, db, user, pw, debug=False)

print [u.user_name for u in session.getUsers()]
print [c.page_title for c in session.getPages(session.getPage(title='Geburtstage'), namespace=mediawiki.NS_CATEGORY)]
print [p.page_title for p in session.getPages(session.getPage(title='Geburtstage'), namespace=mediawiki.NS_MAIN)]

