import mysql.connector

conn=mysql.connector.connect(host='localhost',password='Mufaddal1234',user='root')
if conn.is_connected():
    print("connection established....")
