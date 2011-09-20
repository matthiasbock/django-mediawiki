# -*- coding: iso-8859-15 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^WikiApps/$',				"Django.WikiApps.main.index"),

#	(r'^WikiApps/AutoLogin$',			"Django.WikiApps.Wiki.AutoLogin"),	# meldet den Nutzer Matthias automatisch am Wiki an
#	(r'^WikiApps/RenameFile$',			"Django.WikiApps.Wiki.RenameFile"),	# kann hochgeladene Dateien im Wiki umbenennen

	(r'^WikiApps/Alter$',				"Django.WikiApps.Vorlagen.Alter"),
	(r'^WikiApps/BisZumGeburtstag$',		"Django.WikiApps.Vorlagen.BisZumGeburtstag"),

#	(r'^WikiApps/Adressbuch/$',			"Django.WikiApps.Vorlagen.Adressbuch"),
#	(r'^WikiApps/Adressbuch/Import$',		"Django.WikiApps.Vorlagen.AdressbuchImportieren"),	# VCFs
#	(r'^WikiApps/Adressbuch/Export$',		"Django.WikiApps.Vorlagen.AdressbuchExportieren"),

	#(r'^WikiApps/Familienchronik/$',		"Django.WikiApps.Familienchronik..."),
	# ...
)
