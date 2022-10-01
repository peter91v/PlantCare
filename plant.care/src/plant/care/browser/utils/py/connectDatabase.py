import mysql.connector



def connectToDatabase():
    mysql1 = mysql.connector.connect(user='plantcare', password='plantcare',
                              host='192.168.178.85',
                              database='plantcare')
    if(mysql1):
        print("connection successfull")
    else:
        print("failed")

    return mysql1

def closeDatabase(mysql1):
    mysql1.close()
