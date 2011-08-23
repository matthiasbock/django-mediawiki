#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import sys
sys.path.append("/var/www/Django")
from robot import *

import urllib
import time


class Template:												# Vorlage parsen
	def __init__(self, source=None):
		self.fields	= source.lstrip("{").rstrip("}").split("|")
#		for field in self.fields:
#			field = field.strip(" ")


class TemplateTermin:											# Vorlage:Termin
	def __init__(self, Template):
		self.Typ	= self.Tag	= self.Monat	= self.Jahr	= self.Text	= ""
		self.Datum	= time.strptime( "1.1.2011", "%d.%m.%Y" )
		try:
			self.Typ	= Template.fields[1]
			self.Tag	= Template.fields[2]
			self.Monat	= Template.fields[3]
			self.Jahr	= Template.fields[4]
			self.Datum	= time.strptime( self.Tag+"."+self.Monat+"."+self.Jahr, "%d.%m.%Y" )
			self.Text	= Template.fields[5]
		except:
			pass


class TemplateGeburtstag:										# Vorlage:Geburtstag
	def __init__(self, Template):
		self.Tag	= Template.fields[1]
		self.Monat	= Template.fields[2]
		self.Jahr	= Template.fields[3]
		self.Datum	= time.strptime( self.Tag+"."+self.Monat+"."+self.Jahr, "%d.%m.%Y" )


class WikiConnection:

	def __init__(self):
		self.robot = Robot()
		self.login()

	def login(self):
		self.robot.GET("http://localhost/Wiki/index.php?title=Spezial:Anmelden")		# Einloggen
		self.robot.parse()
		form = self.robot.getForm( name="userlogin" )
		form.getElement( name="wpName" ).value		= "Django"
		form.getElement( name="wpPassword" ).value	= "Django-PW"
		self.robot.submitForm( form )
		#check success

	def open(self, title):
		self.robot.GET("/Wiki/index.php?title="+urllib.quote(title)+"&action=edit")	# Seiten-Text aus dem Bearbeitungsfenster

		self.Page	= ""
		key		= 'name="wpTextbox1"'
		p		= self.robot.Page.find(key)
		if p > -1:
			r	= self.robot.Page.find(">", p)+1
			q	= self.robot.Page.find("</textarea>", p)
			self.Page = self.robot.Page[r:q]

		self.robot.GET("/Wiki/index.php/"+urllib.quote(title))

		self.Categories	= []									# Unterkategorien
		key		= '<div id="mw-subcategories">'
		p		= self.robot.Page.find(key)
		if p > -1:
			q	= self.robot.Page.find("</div>", p)
			div	= self.robot.Page[p:q]
			key	= 'title="'
			r	= div.find(key)
			while r > -1:
				r += len(key)
				s = div.find('"', r)
				self.Categories.append( div[r:s] )
				r = div.find(key, s)

		self.Pages	= []									# Seiten in dieser Kategorie
		key		= '<div id="mw-pages">'
		p		= self.robot.Page.find(key)
		if p > -1:
			q	= self.robot.Page.find('</div>', p)
			div	= self.robot.Page[p:q]
			key	= 'title="'
			r	= div.find(key)
			while r > -1:
				r += len(key)
				s = div.find('"', r)
				self.Pages.append( div[r:s] )
				r = div.find(key, s)

		self.Media	= []									# Medien in dieser Kategorie
		key		= '<div id="mw-category-media">'
		p		= self.robot.Page.find(key)
		if p > -1:
			q	= self.robot.Page.find('</table>', p)
			div	= self.robot.Page[p:q]
			key1	= '<div class="gallerytext">'
			key2	= 'title="'
			r	= div.find(key1)
			while r > -1:
				s = div.find(key2, r)+len(key2)
				t = div.find('"', s)
				self.Media.append( div[s:t] )
				u = div.find("</td>", t)
				r = div.find(key1, u)


	def findTemplates(self, name):									# alle Vorlagen im Seitentext finden
		result	= []
		p	= self.Page.find("{{")
		while p > -1:
			q = self.Page.find("}}", p)+2
			result.append( Template(self.Page[p:q]) )
			p = self.Page.find("{{", q)
		return result

	def saveChanges(self, comment):									# Seite speichern
		pass		# POST changes

	def __del__(self):
		del self.robot


# direkt mit Datenbankzugriff wäre auch denkbar:
#	params["Geburtstage"] = []
#	links = Categorylinks.objects.filter( cl_to="Geburtstage" )
#	for link in links:
#		revisions = Revision.objects.filter( rev_page=link.cl_from )
#		latest = revisions[revisions.count()-1]
#		text = " "+Text.objects.get( id=latest.rev_text_id ).old_text
#		q = -1
#		p = text.find("{{Geburtstag")+2
#		if p == -1:
#			p = text.find("{{ Geburtstag")+2
#		while p > q:
#			q = text.find("}}", p)
#			template = text[p:q].split("|")
#			tag = template[1]
#			monat = template[2]
#			jahr = template[3]
#			page = Page.objects.get( id=link.cl_from )
#			title = page.page_title.split("_")
#			vorname = title[0]
#			try:
#				nachname = title[1]
#			except:
#				pass
#			params["Geburtstage"].append( vorname+" "+nachname+":"+str(tag)+"."+str(monat)+"."+str(jahr) )
#			p = text.find("{{Geburtstag", q)+2
#			if p <= q:
#				p = text.find("{{ Geburtstag")+2

