import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tsaro@9010787282",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)