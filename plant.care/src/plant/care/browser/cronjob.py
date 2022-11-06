# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import json
import time
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity, insertData
from multiprocessing import Process
import paho.mqtt.client as mqtt


from plant.care.browser.utils.py.configs import ConfigFunctions

class CronJobView(BrowserView, ConfigFunctions):
    def __call__(self, *args, **kwargs):
        self.config_json = self.read_config()
        #self.config_json['broker'] = '192.168.178.120'
        print('We Start',self.config_json)
        ##msg = subscribe.simple(self.config_json['topic'], hostname=self.config_json['broker'], auth = {'username':self.config_json['username'], 'password':self.config_json['password']} )
        BROKER_ADDRESS = "192.168.178.120"
        BROKER_PORT = 1883
        max_run = 30
        x = ClientHelp('STO_MQTT',BROKER_ADDRESS,BROKER_PORT,max_run)
        p = Process(target=x.run())
        p.start()
        p.join()

        return super(CronJobView, self).__call__(*args, **kwargs)


class ClientHelp():
    def on_message(self, client, userdata, message):
        msg = message.payload.decode()
        dict = json.dumps(msg)
        print("Received message '" + str(msg) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))
        if "no_sens" in dict:
            print("kein Sensor")
            self.stop()

    def on_connect(self, client, userdata, flags, rc):
        print("connected")
        client.username_pw_set("pico", "plantcare")
        self.subscribe("hello")

    def subscribe(self, topic):
        self.client.subscribe(self.topic_prefix + topic)

    def publish(self, topic, payload):
        print('publish',self.rounds)
        self.client.publish(self.topic_prefix + topic, payload=payload)

    def __init__(self, name,BROKER_ADDRESS,BROKER_PORT,max_run):
        #Thread.__init__(self, name=name)
        self.rounds = 0
        self.max_run = max_run
        self.topic_prefix = ''
        self.running = False
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(BROKER_ADDRESS, BROKER_PORT,1)
        self.client.loop_start()
        self.running = True

    def run(self):
        while self.running:
            #self.publish("hello", "message")
            time.sleep(5)
            if self.rounds >= 10:
                self.stop()
            self.rounds = self.rounds + 5

    def stop(self):
        if self.running:
            self.running = False
            print("Ending and cleaning up")
            self.client.disconnect()
