# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView

class TestView(BrowserView):
    """ eine test view
    """
    def __call__(self, *args, **kwargs):
        return super(TestView, self).__call__(*args, **kwargs)
