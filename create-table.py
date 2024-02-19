import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255), fav INT(11))")

# mycursor.execute("ALTER TABLE custom ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")