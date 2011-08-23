# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
import Django.wiki as wiki
from Django.WikiApps.models import *

import datetime

def kalender( params ):
	return render_to_response("Kalender.html", params)


def Kalender( request ):
	params			= {}
	params["Termine"]	= []
	w			= wiki.WikiConnection()
	w.open("Kategorie:Termine")
	RelevantPages		= w.Categories + w.Pages + w.Media
	for page in RelevantPages:
		w.open( page )
		for Template in w.findTemplates("Termin"):
			Termin = wiki.TemplateTermin( Template )
			params["Termine"].append( { "date":Termin.Datum, "text":Termin.Text })
#	params["Zeilen"]	= []
#	Spalten			= 7
	
	return kalender(params)


def Geburtstagskalender( request ):
	params			= {}
	w			= WikiConnection()
	w.open("Kategorie:Geburtstage")
	params["Geburtstage"]	= []
	for Page in w.Categories:
		w.open(Page)
		for Template in w.findTemplates("Geburtstag"):
			Geburtstag = TemplateGeburtstag( Template )
			params["Termine"].append({ "name":Page.split(":")[1], "date":Geburtstag.Datum })
	return Kalender(params)


def Alter( request ):
	params = {}
	Tag 	= int( request.GET.get("Tag") )
	Monat 	= int( request.GET.get("Monat") )
	Jahr 	= int( request.GET.get("Jahr") )
	Heute 	= datetime.date.today()
	params["Alter"] = Heute.year - Jahr	# angenommen, sie hatte dieses Jahr schon Geburtstag
	if Heute.month < Monat:			# ihr Geburtsmonat war noch nicht
		params["Alter"] = params["Alter"]-1
	elif Heute.month == Monat:		# sie hat diesen Monat Geburtstag
		if Heute.day < Tag:		# hatte aber noch nicht
			params["Alter"] = params["Alter"]-1
	return render_to_response("Alter.html", params)


def BisZumGeburtstag( request ):
	params = {}
	params["Tage"] = 0
	return render_to_response("BisZumGeburtstag.html", params)


