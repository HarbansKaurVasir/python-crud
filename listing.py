import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()
que = "SELECT * FROM custom"
# mycursor.execute("SELECT * FROM custom")
mycursor.execute(que)
myresult = mycursor.fetchall()

dict = {}
# empty dictionary

for value in myresult:
   
    name = value[0]  
    address = value[1]  
    dict[name] = [address]

print([dict])