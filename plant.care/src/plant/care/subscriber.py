# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2019 Metropol Informatik & Handels GesmbH.
#
# Testumfeld f. hoehere Wartung
##############################################################################
"""Access control package.
"""
from zope.browserresource.file import FileResource
from Products.Five.browser import BrowserView
from Products.PageTemplates.PageTemplate import PageTemplate

#-------------------------------------------------------
# Do checks at Zope IPubSuccess (Publication Success)
#-------------------------------------------------------
def ibm_renderAtPub(event):
    request = event.request
    PathOnly = request.get('PATH_INFO', None)

    #**************************************************
    # TODO read sensors should be not a view, but at the moment ok
    # call with curl
    #**************************************************
    type1 = request.environ.get('HTTP_USER_AGENT', None)
    if type1 == None: return 
    if 'curl' in type1: return


    #**************************************************
    # User login only for BrowserViews, not for files, images, ...
    #**************************************************
    start_path = False
    published = request.get('PUBLISHED', None)
    if isinstance(published, FileResource):
        return
    elif PathOnly == '' or PathOnly =='/':
        start_path = True
    else:
        return 

    #**************************************************
    # no path enries, so we redirect
    #**************************************************
    if start_path:
        event.request.RESPONSE.redirect('/@@plantcare.home')
