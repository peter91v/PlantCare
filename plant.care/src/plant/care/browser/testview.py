# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
import spidev
import os
import time

delay = 0.2

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def readChannel(channel):
    val = spi.xfer2([1,(8+channel)<<4,0])
    data = ((val[1]&3)<< 8) + val[2]
    return data
    
class TestView(BrowserView):
    """ eine test view
    """
    def __call__(self, *args, **kwargs):
        return super(TestView, self).__call__(*args, **kwargs)

    def testread(self):
        mydict = []
        try:
            for x in range(0,5):
                val = readChannel(0)
                mydict.append(val)
                print(val)
                time.sleep(1)
        except KeyboardInterrupt:
            print ("cancel")
        print (mydict)
        return mydict
