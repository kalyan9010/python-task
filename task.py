import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tsaro@9010787282"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
