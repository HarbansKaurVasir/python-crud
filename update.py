import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()

sql = "UPDATE custom SET name = 'harbans' WHERE name = 'harshit'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")