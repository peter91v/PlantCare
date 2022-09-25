# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView

class HomeView(BrowserView):
    """ eine test view
    """
    def __call__(self, *args, **kwargs):
        return super(HomeView, self).__call__(*args, **kwargs)
