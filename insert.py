import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="mydata"
)

mycursor = mydb.cursor()

sql = "INSERT INTO custom (name, address) VALUES (%s, %s)"
val = [
    ('harnam' ,'milerganj'),
    ('h' ,'miler'),
    ('ha' ,'mile'),
    ('har' ,'milerga'),
    ('harn' ,'milergan')
]
    # ("harbans", "Highway 21")
# mycursor.execute(sql, val)
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")