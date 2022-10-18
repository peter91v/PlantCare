# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import json
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity, insertData
import paho.mqtt.client as mqtt_client
import paho.mqtt.subscribe as subscribe
from plant.care.browser.utils.py.configs import ConfigFunctions

class CronJobView(BrowserView, ConfigFunctions):
    def __call__(self, *args, **kwargs):
        self.config_json = self.read_config()

        print(self.getMessagePico())
        msg = self.getMessagePico()
        for i in msg:
            insertData(i, msg[i])
        return super(CronJobView, self).__call__(*args, **kwargs)
        
    def getMessagePico(self):
        msg = subscribe.simple(self.config_json['topic'], hostname=self.config_json['broker'], auth = {'username':self.config_json['username'], 'password':self.config_json['password']} )
        return json.loads(msg.payload.decode('utf8'))