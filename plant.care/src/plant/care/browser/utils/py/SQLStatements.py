from plant.care.browser.utils.py.connectDatabase import connectToDatabase as cdb
from datetime import date, datetime
def insertDatabase(id, name, hum, dry, wet):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Sensors (ID, SensorName, Humidity, SensorDry, SensorWet) VALUES (%s, %s, %s, %s, %s)'
    val = (id, name, hum, dry, wet)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(temp['code'], "was inserted.")
    mycursor.close()
    mydb.close()
    return True

def getMoisturValues(temp):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'SELECT SensorDry, SensorWet FROM Sensors WHERE ID = %s'
    val = (temp,)
    mycursor.execute(sql, val)
    row = mycursor.fetchall()
    
    mydb.commit()
    mycursor.close()
    mydb.close()
    return row

def updateSensor(dry, wet, id):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'UPDATE Sensors set SensorDry = %s, SensorWet = %s WHERE ID = %s'
    val = (dry, wet, id)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(temp['code'], "was updated.")
    mycursor.close()
    mydb.close()
    return True

def updateHumidity(hum, id):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'UPDATE Sensors set Humidity = %s WHERE ID = %s'
    val = (hum, id)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(temp['code'], "was updated.")
    mycursor.close()
    mydb.close()
    return True

def getHumidity(id):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'select SensorName, Humidity from Sensors'
    val = ()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    mydb.commit()
    #print(temp['code'], "was updated.")
    mycursor.close()
    mydb.close()
    return myresult

def insertData(Sensor, humidity):
    mydb = cdb()
    mycursor = mydb.cursor()
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    print("date = " + str(date) + ", time = " + str(time) + ", humidity = "+ str(humidity) + ", sensor = " + str(Sensor))
    sql = 'INSERT INTO Data (humidity, date, time, Sensor) VALUES (%s, %s, %s, %s);'
    val = (humidity, date, time, Sensor)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(temp['code'], "was inserted.")
    mycursor.close()
    mydb.close()
    return True

def getHumidityData(sensor):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = ' select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = %s order by d.date desc, d.time desc limit 1440) d1 order by d1.date asc, d1.time asc'
    val = (sensor,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    result = []
    for i in myresult:
        result.append({"hum": i[0], "time": dateTimeDeltatoTime(i[1])})
    mydb.commit()
    mycursor.close()
    mydb.close()
    return result

def getsensors():
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'select SensorName from Sensors'
    val = ()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    result = []

    for i in myresult:
        for s in i:
            result.append(s)

    mydb.commit()
    mycursor.close()
    mydb.close()
    return result

def dateTimeDeltatoTime(delta):
    s = delta.total_seconds()
    # hours
    hours = s // 3600
    # remaining seconds
    s = s - (hours * 3600)
    # minutes
    minutes = s // 60
    # remaining seconds
    seconds = s - (minutes * 60)
    # total time
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

def getsensorsHome():
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = 'SELECT S.SensorName, d.humidity from Sensors S inner join Data d on SensorName = Sensor order by d.date desc ,d.time desc limit 3'
    val = ()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    result = []
    mydb.commit()
    mycursor.close()
    mydb.close()
    return myresult