# -*- coding: utf-8 -*-
from pydoc import cli
from Products.Five.browser import BrowserView
import os
import time
import plant.care.browser.utils.py.connectDatabase as cdb
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity,insertDatabase, getHumidityData, getsensors
import paho.mqtt.client as mqtt_client
import json
import paho.mqtt.subscribe as subscribe
from plant.care.browser.utils.py.configs import ConfigFunctions


class ChartView(BrowserView,ConfigFunctions):
    """ eine test view
    """

    def __call__(self, *args, **kwargs):

        self.config_json = self.read_config()
        
        return super(ChartView, self).__call__(*args, **kwargs)


    def getSensHum(self):
        data = getHumidity(0)
        datadict = []
        for i in data:
            x = {'sensname': i[0], 'value': i[1]}
            datadict.append(x)
        return datadict
    
   

    def getdata(self):
        sensors = getsensors()
        dataset = []
        colors = ["#990000", "#3528AC", "#2FB05A"]
        x = {
            "label": 'My First dataset',
            "fill": 'false',
            "backgroundColor": 'rgb(255, 99, 132)',
            "borderColor": 'rgb(255, 99, 132)',
            "data": "hum",
          }
        s = 0
        #sensors = sensors[0]
        for sen in sensors:
          
            temp = getHumidityData(sen)
            tempdata = x.copy()
            time = []

            hum = []
            for i in temp:
                hum.append(i['hum'])
                time.append(i['time'])

            tempdata["data"] = hum
            tempdata["borderColor"] = colors[s]
            tempdata["backgroundColor"] = colors[s]
            tempdata["label"] = sen

            s +=1
            dataset.append(tempdata)
        data = {"dataset": dataset, "time" : time}
        return data
    