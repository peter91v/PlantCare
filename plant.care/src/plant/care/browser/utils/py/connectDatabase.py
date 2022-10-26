
import imp
import mysql.connector
import socket


def connectToDatabase():
    mysql1 = mysql.connector.connect(user='plantcare', password='plantcare',
                              host=get_my_ip(),
                              database='plantcare')
    if(mysql1):
        print("connection successfull")
    else:
        print("failed")

    return mysql1

def closeDatabase(mysql1):
    mysql1.close()

def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

