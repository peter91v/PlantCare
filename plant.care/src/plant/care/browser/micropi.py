# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import json
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity


class RaspiPicoView(BrowserView):
    def __call__(self, *args, **kwargs):

        if 'sensid' in self.request.form:
            print('Sensorid=',self.request.form['sensid'])
            updateHumidity(self.request.form['sensid'], 0)
        #return super(RaspiPicoView, self).__call__(*args, **kwargs)