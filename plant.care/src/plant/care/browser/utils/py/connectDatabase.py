import mysql.connector



def connectToDatabase():
  #  mysql1 = mysql.connector.connect(user='plantcare', password='plantcare',
                            #   host='127.0.0.1',
                            #   database='plantcare')
    # if(mysql1):
    #     print("connection successfull")
    # else:
    #     print("failed")

    return "mysql1"

def closeDatabase(mysql1):
    #mysql1.close()
    print(mysql1)
