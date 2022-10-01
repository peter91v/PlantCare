# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import json

class RaspiPicoView(BrowserView):
    def __call__(self, *args, **kwargs):
        print('==============>>>',self.request.form)
        if 'sensid' in self.request.form:
            print('Sensorid=',self.request.form['sensid'])
        #return super(RaspiPicoView, self).__call__(*args, **kwargs)