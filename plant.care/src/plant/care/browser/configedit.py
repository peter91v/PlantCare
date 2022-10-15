# -*- coding: utf-8 -*-
import json
from Products.Five.browser import BrowserView
from plant.care.browser.utils.py.configs import ConfigFunctions

class ConfigEditView(BrowserView,ConfigFunctions):
    def __call__(self, *args, **kwargs):
        self.config_json = self.read_config()
        self.error_msg = ''
        if 'config_json' in self.request.form and self.request.method == 'POST':
            try:
                self.config_json = json.loads(self.request.form["config_json"])
                self.update_config()
            except:
                self.error_msg = 'Es gab ein Problem mit der JSON Formatierung!!!!!!'
            self.config_json = self.read_config()

        return super(ConfigEditView, self).__call__(*args, **kwargs)

    #---------------------------------------------------
    # return error msg string
    #---------------------------------------------------
    def get_errorMessage(self):
        return self.error_msg
