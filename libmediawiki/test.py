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

print [u.user_name for u in wiki.getUsers()]
print str(len(wiki.getPages()))+' pages total'
print [c.page_title for c in wiki.getPages(wiki.getPage(title='Geburtstage'), namespace=NS_CATEGORY)]
print [p.page_title for p in wiki.getPages(wiki.getPage(title='Geburtstage'), namespace=NS_MAIN)]

print [r.rev_comment for r in wiki.getPage(title='Geburtstage', namespace=NS_CATEGORY).getRevisions()]
