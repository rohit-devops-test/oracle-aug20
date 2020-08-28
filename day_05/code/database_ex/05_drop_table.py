import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers2"

mycursor.execute(sql)
