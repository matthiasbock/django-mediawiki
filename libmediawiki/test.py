#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import mediawiki

session = mediawiki.Session( host='localhost', database='wiki', username='john', passwort='doe' )

print session.getUsers()
print session.getCategories('Geburtstage')
print session.getPages('Geburtstage')

