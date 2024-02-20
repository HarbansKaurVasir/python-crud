import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()

# que = "SELECT * FROM custom "
# mycursor.execute("SELECT * FROM custom")
mycursor.execute("SELECT * FROM custom ")
myresult = mycursor.fetchall()

data_list = []
# empty dictionary
for  value in myresult:
    dic = {
        'name' : value[0],
        'address' : value[1],
        'id' : value[2]
      }
    data_list.append(dic)
print(data_list)