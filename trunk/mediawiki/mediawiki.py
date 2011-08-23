# -*- coding: iso-8859-15 -*-

from Django.globals import *
from Django.WikiApps.models import *

FilePrefix	= "Datei:"
WikiImagePath	= "/var/www/Wiki/images"


class mediawikiPage:

	def __init__(self, title=None):
		self.title	= ""
		self.opened	= False
		self.text	= ""
		self.DEBUG	= ""
		if title is not None:
			self.open( title )

	def exists(self, title):
		return True

	def open(self, title):
		self.opened = False
		if self.exists( title ):
			pass
		return self.opened

		
class mediawikiFile:

	def __init__(self, title=None):
		self.title	= ""
		self.opened	= False
		self.location	= ""
		self.file	= None
		self.page	= None
		self.DEBUG	= ""
		if title is not None:
			self.open( title )

	def exists(self, title):
		return True

	def open(self, title):
		self.opened = False
		self.DEBUG += "Open file "+title+" ...\n"
		if self.exists( title ):
			self.title	= title
#			self.location	= "" #... Link auf die physische Datei
#			self.file	= open( self.location, "r" )
#			self.page	= "" #... Abruf aus der Datenbank
			self.opened	= True
		return self.opened

	def rename(self, newname):
		self.DEBUG += "Rename file to "+newname+" ...\n"
		if not self.opened:
			self.DEBUG += "Error: No file opened\n"
			return False
		if self.exists( newname ):
			self.DEBUG += "Error: File exists\n"
			return False

		result = ""

		# ID=2	cl_from=1405	cl_to=Stefan_Grahamer	cl_sortkey=Bild:Img 1164.jpg	cl_timestamp=2009-01-16 06:02:25
		for c in categorylinks.objects.using( WikiDB ).filter( cl_sortkey=FilePrefix+oldname ):
			c.cl_sortkey = FilePrefix+newname
			result += "category_links: ID "+str( c.id )+": cl_sortkey changed\n"
#			c.save()

		for img in image.objects.using( WikiDB ).filter( img_name=oldname.replace(" ", "_") ):
			img.img_name = newname.replace(" ", "_")
			result += "image: ID "+str( img.id )+": img_name changed\n"
#			img.save()

		for l in logging.objects.using( WikiDB ).filter( log_title__contains=FilePrefix+oldname ):
			l.log_title = l.log_title.replace( FilePrefix+oldname, FilePrefix+newname )
			result += "logging: log_id "+str( l.id )+": log_title changed\n"
#			l.save()

		for p in page.objects.using( WikiDB ).filter( page_title=oldname ):
			p.page_title = newname
			result += "page: page_id "+str( p.id )+": page_title changed\n"
#			p.save()

		for s in searchindex.objects.using( WikiDB ).filter( si_title=oldname.lower().replace(".", " ") ):
			s.si_title = newname.lower().replace(".", " ")
			result += "searchindex: si_page "+str( s.id )+": si_title changed\n"
#			s.save()

		oldpath = WikiImagePath+"/"+oldname
		newpath = WikiImagePath+"/"+newname
#		os.path.rename( oldpath, newpath )

		result += "Renamed "+oldpath+" to "+newpath+"\n"

		WikiAppsLog.objects.create( vorgang="rename file\n"+FilePrefix+self.title+"\nto\n"+FilePrefix+newname, ergebnis=result )
		self.DEBUG += result

		self.open( newname )

class mediawikiCategory:
	...
	__init__

	open

	pages

	categories



class mediawikiSearch:

	findpages

	findcategories

	find


