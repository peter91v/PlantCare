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
    print("date = " + str(date) + ", time = " + str(time) +
          ", humidity = " + str(humidity) + ", sensor = " + str(Sensor))
    sql = 'INSERT INTO Data (humidity, date, time, Sensor) VALUES (%s, %s, %s, %s);'
    val = (humidity, date, time, Sensor)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(temp['code'], "was inserted.")
    mycursor.close()
    mydb.close()
    return True


def getHumidityData(sensor, count, dateVon, dateBis, timeVon, timeBis, step):
    mydb = cdb()
    mycursor = mydb.cursor()
    sql = ""
    tCount = count
    print("count", count, type(count))
    print("step", step, type(step))
    if (step != 0 and count != ''):
        tCount = int(int(count) * (int(step / 2)))
        print('tcount', tCount)
    if (dateVon != "" and dateBis != "" and count != "" and timeVon != "" and timeBis != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and date >= '{1}' and date <= '{2}' and time >= '{3}' and time <= '{4}' order by d.date desc, d.time desc limit {5} ) d1 order by d1.date asc, d1.time asc""".format(
            sensor, dateVon, dateBis, timeVon[:5], timeBis[:5], tCount)
    elif (dateVon != "" and dateBis != "" and timeVon != "" and timeBis != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and date >= '{1}' and date <= '{2}' and time >= '{3}' and time <= '{4}' order by d.date desc, d.time desc) d1 order by d1.date asc, d1.time asc""".format(
            sensor, dateVon, dateBis, timeVon[:5], timeBis[:5])
        print(sql)
    elif (dateVon != "" and dateBis != "" and count != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and date >= '{1}' and date <= '{2}' order by d.date desc, d.time desc limit {3} ) d1 order by d1.date asc, d1.time asc""".format(
            sensor, dateVon, dateBis, tCount)
    elif (dateVon != "" and dateBis != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and date >= '{1}' and date <= '{2}' order by d.date desc, d.time desc) d1 order by d1.date asc, d1.time asc""".format(
            sensor, dateVon, dateBis)
    elif (count != "" and timeVon != "" and timeBis != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and time >= '{1}' and time <= '{2}' order by d.date desc, d.time desc limit {3} ) d1 order by d1.date asc, d1.time asc""".format(
            sensor, timeVon[:5], timeBis[:5], tCount)
    elif (timeVon != "" and timeBis != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and time >= '{1}' and time <= '{2}' order by d.date desc, d.time desc ) d1 order by d1.date asc, d1.time asc""".format(
            sensor, timeVon[:5], timeBis[:5])
    elif (count != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' order by d.date desc, d.time desc limit {1} ) d1 order by d1.date asc, d1.time asc""".format(
            sensor, tCount)
    elif (dateVon != "" and timeVon != ""):
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' and date >= '{1}' and time >= '{2}' order by d.date desc, d.time desc) d1 order by d1.date asc, d1.time asc""".format(
            sensor, dateVon, timeVon)

    else:
        sql = """select d1.humidity, d1.time from (select d.humidity, d.date, d.time from Data d where sensor = '{0}' order by d.date desc, d.time desc) d1 order by d1.date asc, d1.time asc""".format(
            sensor)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    result = []
    for i in myresult:
        if (step != 0):
            for x in range(0, 60, step):
                if (x < 10):
                    x = '0' + str(x)
                if ((str(x) in str(dateTimeDeltatoTime(i[1])[3:5]))):
                    result.append(
                        {"hum": i[0], "time": dateTimeDeltatoTime(i[1])})
        if step == 0:
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


def getTableDate(sTable, sen):
    mydb = cdb()
    mycursor = mydb.cursor()
    #print(startdate, enddate, time)
    sql = """SELECT DISTINCT date FROM {0} where Sensor = '{1}' order by date desc;""".format(
        sTable, sen)
    # params = [sTable, startdate, enddate, time]
    mycursor.execute(sql)
    row = mycursor.fetchall()

    mydb.commit()
    mycursor.close()
    mydb.close()
    return row


def getTableTime(sTable, sen):
    mydb = cdb()
    mycursor = mydb.cursor()
    #print(startdate, enddate, time)
    sql = """SELECT DISTINCT time FROM {0} where Sensor = '{1}' order by time asc;""".format(
        sTable, sen)
    # params = [sTable, startdate, enddate, time]
    mycursor.execute(sql)
    row = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return row


def getCounter(sTable, sen):
    mydb = cdb()
    mycursor = mydb.cursor()
    #print(startdate, enddate, time)
    sql = """select count(*) from {0} where Sensor = '{1}' group by Sensor;""".format(
        sTable, sen)
    # params = [sTable, startdate, enddate, time]
    mycursor.execute(sql)
    row = mycursor.fetchone()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return row
