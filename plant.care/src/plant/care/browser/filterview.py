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


class FilterView(BrowserView,ConfigFunctions):
    """ eine test view
    """

    def __call__(self, *args, **kwargs):
       
        self.config_json = self.read_config()
        
        return super(FilterView, self).__call__(*args, **kwargs)


    def getSensHum(self):
        data = getHumidity(0)
        datadict = []
        for i in data:
            x = {'sensname': i[0], 'value': i[1]}
            datadict.append(x)
        return datadict
    
    def testread(self):
        # self.client = self.connect_mqtt()
        # self.client.loop_start()
        # self.mes = self.subscribe(self.client)
        # #self.client.loop_stop(force=False)
        # print(self.mes)
        mydict = self.getSensHum()
        # msg = subscribe.simple(self.config_json['topic'], hostname=self.config_json['broker'], auth = {'username':self.config_json['username'], 'password':self.config_json['password']} )
        # #print("%s" % (msg.payload.decode('utf8')))
        # x = json.loads(msg.payload.decode('utf8'))
        
        # insertDatabase(1, "Sensor2", 45, 65535, 42954)
        # try:
        #     # for x in range(0,5):
        #     #     val = spi.readChannel(0)
        #     #     mydict.append(val.value)
               
        #     #     time.sleep(0.2)
        #     mydict.append(x)
        #     print(x)
        # except KeyboardInterrupt:
        #     print ("cancel")
        
        # mydb = cdb.connectToDatabase()
        # cdb.closeDatabase(mydb)
        #cS.calibrateSensor(0)
        #print(cS.calclulateHumidity(0, spi.readChannel(0)))
        # print('Raw ADC Value: ', channel.value)
        # print('ADC Voltage: ' + str(channel.voltage) + 'V')
        return mydict

