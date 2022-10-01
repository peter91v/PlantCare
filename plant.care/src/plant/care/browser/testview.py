# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import os
import time
import plant.care.browser.utils.py.connectDatabase as cdb
import plant.care.browser.utils.py.spi as spi
import plant.care.browser.utils.py.calibrateSensor as cS

    
class TestView(BrowserView):
    """ eine test view
    """
    hum = hum = request.form['sensid']
    def __call__(self, *args, **kwargs):
        if 'sensid' in self.request.form:
            print('Sensorid=',self.request.form['sensid'])
            hum = self.request.form['sensid']
        return super(TestView, self).__call__(*args, **kwargs)

    def testread(self):
        
        mydict = []
        try:
            # for x in range(0,5):
            #     val = spi.readChannel(0)
            #     mydict.append(val.value)
               
            #     time.sleep(0.2)
            mydict.append(self.hum)
        except KeyboardInterrupt:
            print ("cancel")
        
        mydb = cdb.connectToDatabase()
        cdb.closeDatabase(mydb)
        #cS.calibrateSensor(0)
        #print(cS.calclulateHumidity(0, spi.readChannel(0)))
        # print('Raw ADC Value: ', channel.value)
        # print('ADC Voltage: ' + str(channel.voltage) + 'V')
        return mydict
