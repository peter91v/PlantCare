# -*- coding: utf-8 -*-
import imp
from Products.Five.browser import BrowserView
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity, getsensorsHome
import requests
from plant.care.browser.utils.py.configs import ConfigFunctions
import paho.mqtt.client as mqtt_client
import json
import paho.mqtt.subscribe as subscribe
from plant.care.browser.utils.py.configs import ConfigFunctions

class HomeView(BrowserView, ConfigFunctions):
    """ eine test view
    """
    def __call__(self, *args, **kwargs):
        self.config_json = self.read_config()

        return super(HomeView, self).__call__(*args, **kwargs)
    
    def getSensHum(self):
            data1 = getsensorsHome()
            print(data1)
            datadict = {}
            # msg = subscribe.simple(self.config_json['topic'], hostname=self.config_json['broker'], auth = {'username':self.config_json['username'], 'password':self.config_json['password']} )
            # data = json.loads(msg.payload.decode('utf8'))
            for i in data1:
                print(i)
                x = {i[0]:{ 'value': int(round(i[1])), 'text': 'text' }}
                datadict.update(x)
            return datadict
        
    def getHumidity(self):
            #humDict =  {'sensor1': {'value':80, 'text': 'text'}, 'sensor2': {'value':63, 'text': 'text1'}, 'sensor3': {'value':15, 'text': 'text2'}}
            # Sort Dictionary by Sensorkey
            SensDict = self.getSensHum()
            sorted_dict = {k: SensDict[k] for k in sorted(SensDict)}
            return sorted_dict
