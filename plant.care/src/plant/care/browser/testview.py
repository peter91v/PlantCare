# -*- coding: utf-8 -*-
from pydoc import cli
from Products.Five.browser import BrowserView
import os
import time
import plant.care.browser.utils.py.connectDatabase as cdb
from plant.care.browser.utils.py.SQLStatements import updateHumidity, getHumidity, insertDatabase, dateTimeDeltatoTime, getHumidityData, getsensors, getTableDate, getTableTime, getCounter
import paho.mqtt.client as mqtt_client
import json
import paho.mqtt.subscribe as subscribe
from plant.care.browser.utils.py.configs import ConfigFunctions


class TestView(BrowserView, ConfigFunctions):
    def __call__(self, *args, **kwargs):

        self.config_json = self.read_config()
        self.callSensor = ""
        self.count = ""
        self.dateVon = ""
        self.dateBis = ""
        self.timeVon = ""
        self.timeBis = ""
        self.sumOfValues = 100
        self.title = ""
        self.step = 0
        self.description = ""
        self.checkbox = "None"
#{'Sensors': 'Sensor1', 'count': '', 'dateVon': '', 'dateBis': '', 'timevon': '', 'timeBis': ''}

        if self.request.method == 'POST':
            print(self.request.form)

            if "Sensors" in self.request.form and "count" in self.request.form and "dateVon" in self.request.form and "timevon" in self.request.form:
                self.callSensor = self.request.form["Sensors"]
                self.count = self.request.form["count"]
                self.dateVon = self.request.form["dateVon"]
                self.dateBis = self.request.form["dateBis"]
                self.timeVon = self.request.form["timevon"]
                self.timeBis = self.request.form["timeBis"]
            if "step" in self.request.form:
                if (self.request.form["step"] != ''):
                    self.step = int(self.request.form["step"])
            print(self.callSensor)
            print(self.count)
            print(self.dateVon)
            print("post", self.sumOfValues)
        return super(TestView, self).__call__(*args, **kwargs)

    def get_selected_sensor(self):
        return self.callSensor

    def get_selected_counter(self):

        return self.count

    def get_selected_dateBis(self):
        return self.dateBis

    def get_selected_dateVon(self):
        return self.dateVon

    def get_selected_timeVon(self):
        return self.timeVon

    def get_selected_timeBis(self):
        return self.timeBis

    def getSensHum(self):
        data = getHumidity(0)
        datadict = []
        for i in data:
            x = {'sensname': i[0], 'value': i[1]}
            datadict.append(x)
        return datadict

    def getTable(self):
        sensors = getsensors()
        datadict = []
        for i in sensors:
            x = {'table': i, 'comment': i}
            datadict.append(x)
        return datadict

    def makeCounter(self):
        counter = []

        x = 10
        z = {'countr': x, }
        sum = getCounter("Data", "sensor1")
        counter.append(z)
        while x <= sum[0]:
            if (x < 100):
                x += 10
            elif (x < 1000):
                x += 100
            else:
                x += 500
            y = {'countr': x, }
            counter.append(y)
        return counter

    def getTableDates(self):
        datadict = []
        datadict.append({'Date': '-'})

        if self.callSensor != "":
            data = getTableDate("Data", self.callSensor)
        else:
            data = getTableDate("Data", "sensor1")
        for i in data:
            x = {'Date': i[0]}
            datadict.append(x)
        return datadict

    def getTableTimes(self):
        datadict = []
        datadict.append({'Time': '-'})
        lastTimeVal = ""
        if self.callSensor != "":
            data = (getTableTime("Data", self.callSensor))
        else:
            data = (getTableTime("Data", "sensor1"))
        for i in data:
            x = {'Time': dateTimeDeltatoTime(i[0])[:5]}

            if (lastTimeVal != x):
                y = {'Time': (x['Time'] + ":00")}
                datadict.append(y)
                lastTimeVal = x
        return datadict

    def getSteps(self):
        datadict = []
        step = [5, 10, 30, 60]
        for y in step:
            x = {'Step': y}
            datadict.append(x)

        return datadict

    # def getdata(self):
    #     sensors = getsensors()
    #     dataset = []
    #     colors = ["#990000", "#3528AC", "#2FB05A"]
    #     x = {
    #         "label": 'My First dataset',
    #         "fill": 'false',
    #         "backgroundColor": 'rgb(255, 99, 132)',
    #         "borderColor": 'rgb(255, 99, 132)',
    #         "data": "hum",
    #       }
    #     s = 0
    #     #sensors = sensors[0]
    #     maxrounds = 99999

    #     for sen in sensors:
    #         if self.callSensor != "":
    #             if self.callSensor != sen:
    #                 continue
    #         if self.count != "":
    #             try:
    #                 maxrounds = int(self.count)
    #             except:
    #                 """ """

    #         temp = getHumidityData(sen)
    #         tempdata = x.copy()
    #         time = []

    #         hum = []
    #         #s=0
    #         for i in temp:
    #             hum.append(i['hum'])
    #             time.append(i['time'])
    #             # if s > maxrounds:
    #             #     break
    #             #s=s+1

    #         tempdata["data"] = hum
    #         tempdata["borderColor"] = colors[s]
    #         tempdata["backgroundColor"] = colors[s]
    #         tempdata["label"] = sen

    #         s +=1
    #         dataset.append(tempdata)
    #     data = {"dataset": dataset, "time" : time}
    #     return data
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
            if self.callSensor != "All":
                if self.callSensor != "":
                    if self.callSensor != sen:
                        continue
                if self.count != "":
                    try:
                        maxrounds = int(self.count)
                    except:
                        """ """
            temp = {}
            if self.callSensor != "All" and self.callSensor != "":
                temp = getHumidityData(
                    self.callSensor, self.count, self.dateVon, self.dateBis, self.timeVon, self.timeBis, self.step)
            else:
                temp = getHumidityData(
                    sen, self.count, self.dateVon, self.dateBis, self.timeVon, self.timeBis, self.step)
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

            s += 1
            dataset.append(tempdata)
        data = {"dataset": dataset, "time": time}
        self.sumOfValues = len(data['dataset'][0]['data'])

        return data
