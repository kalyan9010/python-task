import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tsaro@9010787282",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (ID INT, name VARCHAR(255), address VARCHAR(255), job VARCHAR(255),hiredata DATE)")