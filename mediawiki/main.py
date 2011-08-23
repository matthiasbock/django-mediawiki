# -*- coding: iso-8859-15 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from Django.globals import *
from Django.WikiApps.models import *

import datetime


def index( request ):
	return HttpResponseRedirect("Kalender/")

def Login(request):
	LoginURL = "http://localhost/Wiki/index.php/Spezial:Anmelden"
	# get login page
	# post login vars
	# extract cookie from response
	# send cookie to client
	return HttpResponseRedirect("/Wiki/index.php/Spezial:Letzte_%C3%84nderungen")

def RenameFile( request ):
	params = defaults()
	if request.method == "GET":
		return render_to_response("RenameFile.html", params)
	elif request.method == "POST":
		prefix	= "Datei:"
		WikiImagePath = "/var/www/Wiki/images"
		oldname = request.POST.get("oldname").decode("latin1").encode("ascii")
		newname = request.POST.get("newname")
		command = "RenameFile\n"+prefix+oldname+"\nto\n"+prefix+newname
		result = ""
		for Categorylink in Categorylinks.objects.filter( cl_sortkey=prefix+oldname ):
			Categorylink.cl_sortkey = prefix+newname
			result += "category_links: ID "+str(Categorylink.id)+": cl_sortkey changed\n"
#			Categorylink.save()
		for img in Image.objects.filter( img_name=oldname.replace(" ", "_") ):
			img.img_name = newname.replace(" ", "_")
			result += "image: ID "+str(img.id)+": img_name changed\n"
#			img.save()
		for Log in Logging.objects.filter( log_title__contains=prefix+oldname ):
			Log.log_title = Log.log_title.replace( prefix+oldname, prefix+newname )
			result += "logging: log_id "+str(Log.id)+": log_title changed\n"
#			Log.save()
		for page in Page.objects.filter( page_title=oldname ):
			page.page_title = newname
			result += "page: page_id "+str(page.page_id)+": page_title changed\n"
#			page.save()
		for SI in Searchindex.objects.filter( si_title=oldname.lower().replace(".", " ") ):
			SI.si_title = newname.lower().replace(".", " ")
			result += "searchindex: si_page "+str(SI.id)+": si_title changed\n"
#			SI.save()

		oldpath = WikiImagePath+"/"+oldname
		newpath = WikiImagePath+"/"+newname
#		os.path.rename( oldpath, newpath )
		result += "Renamed "+oldpath+" to "+newpath+"\n"

		params["ShowMessage"] = True
		params["Message"] = result.replace("\n","<br/>\n")
		Wikidjangolog.objects.create( vorgang=command, ergebnis=result )

		return render_to_response("RenameFile.html", params)



