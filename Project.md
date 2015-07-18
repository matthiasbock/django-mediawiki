# django-mediawiki #

This Python library shall provide a DAL (database abstraction layer) for your [MediaWiki](http://www.mediawiki.org/) installation.

It enables you to use Django's easy database access methods to create apps and bots capable of reading from and writing to your Wiki, fulfilling more sophisticated tasks than the mediawiki PHP web interface would allow.

The main difference to [other implementations](http://www.mediawiki.org/wiki/API:Client_code#Python) is, that you do not need any PHP, since the database is accessed directly.