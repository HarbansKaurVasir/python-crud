import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydatabase"
)

mycursor = mydb.cursor()    

# mycursor.execute("CREATE DATABASE mydata")

# print("created new database")

'''to show all databases'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)