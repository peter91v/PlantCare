import plant.care.browser.utils.py.spi as spi
from plant.care.browser.utils.py.SQLStatements import insertDatabase, getMoisturValues, updateSensor
import time



def calibrateSensor(channel):    
    moistur_dry = 0
    moistur_wet = 0
    val = spi.readChannel(channel)
    while (val.value > moistur_dry):
        val = spi.readChannel(channel)
        moistur_dry = val.value
        time.sleep(1)
    print("moistur_dry: " + str(moistur_dry))
    print("Put your sensor into a glass of water!")
    moistur_wet = moistur_dry
    time.sleep(60)
    while (moistur_wet > val.value):
        val = spi.readChannel(channel)
        moistur_wet = val.value
        time.sleep(1)
        
    print("moistur_wet: " + str(moistur_wet))
    #insertDatabase(channel, "Sensor1", 0, moistur_dry, moistur_wet)
    updateSensor(moistur_dry, moistur_wet, channel)
    print("Calibrating Successful")
    
def calclulateHumidity(channel, val):
    temp = getMoisturValues(channel)
    print(str(temp[0][0]) + ", " + str(temp[0][1]))
    
    hum =( temp[0][0] - val.value)/(temp[0][0]-temp[0][1])*100
    return hum