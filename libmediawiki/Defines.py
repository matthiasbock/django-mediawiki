#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# adapted from mediawiki/includes/Defines.php

#
# Virtual namespaces don't appear in the page database
#
NS_MEDIA = -2
NS_SPECIAL = -1


#
# Real namespaces
#
# Number 100 and beyond are reserved for custom namespaces
# DO NOT assign standard namespaces at 100 or beyond.
# DO NOT Change integer values as they are most probably hardcoded everywhere
# see bug #696 which talked about that.
#
NS_MAIN = 0
NS_TALK = 1
NS_USER = 2
NS_USER_TALK = 3
NS_PROJECT = 4
NS_PROJECT_TALK = 5
NS_IMAGE = 6
NS_IMAGE_TALK = 7
NS_MEDIAWIKI = 8
NS_MEDIAWIKI_TALK = 9
NS_TEMPLATE = 10
NS_TEMPLATE_TALK = 11
NS_HELP = 12
NS_HELP_TALK = 13
NS_CATEGORY = 14
NS_CATEGORY_TALK = 15

