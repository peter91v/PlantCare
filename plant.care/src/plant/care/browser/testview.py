# -*- coding: utf-8 -*-
from pydoc import cli
from Products.Five.browser import BrowserView
import os
import time
import plant.care.browser.utils.py.connectDatabase as cdb
import plant.care.browser.utils.py.spi as spi
import plant.care.browser.utils.py.calibrateSensor as cS
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity,insertDatabase
import paho.mqtt.client as mqtt_client
import json
import paho.mqtt.subscribe as subscribe
from plant.care.browser.utils.py.configs import ConfigFunctions


class TestView(BrowserView,ConfigFunctions):
    """ eine test view
    """

    def __call__(self, *args, **kwargs):
        self.broker = '192.168.178.85'
        self.port = 1883
        self.topic = "hello"
        self.client_id = 'python-mqtt-1'
        self.username = 'pico'
        self.password = 'plantcare' 
        
        self.config_json = self.read_config()
        
        return super(TestView, self).__call__(*args, **kwargs)


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
        msg = subscribe.simple(self.config_json['topic'], hostname=self.config_json['broker'], auth = {'username':self.config_json['username'], 'password':self.config_json['password']} )
        #print("%s" % (msg.payload.decode('utf8')))
        x = json.loads(msg.payload.decode('utf8'))
        
        print(x)
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

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        x = ""
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            
            return msg.payload.decode('utf8')
        client.subscribe(self.topic)
        x = client.on_message = on_message
        return x

    def run(self):
        client = self.connect_mqtt()
        client.loop_start()
        self.subscribe(client)