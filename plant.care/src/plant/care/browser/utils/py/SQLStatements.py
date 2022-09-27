from plant.care.browser.utils.py.connectDatabase import connectToDatabase as cdb

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