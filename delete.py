import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()

sql = "DELETE FROM custom WHERE id = 3"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")