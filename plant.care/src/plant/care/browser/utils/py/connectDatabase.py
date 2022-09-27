import mysql.connector



def connectToDatabase():
    mysql1 = mysql.connector.connect(user='peter', password='plantcare',
                              host='localhost',
                              database='plantcare')
    # if(mysql1):
    #     print("connection successfull")
    # else:
    #     print("failed")

    return mysql1

def closeDatabase(mysql1):
    mysql1.close()

