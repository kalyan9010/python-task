import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tsaro@9010787282",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (id, name, address, job, hiredata) VALUES (%s, %s,%s, %s ,%s)"
val = [

  (1, "John", "Highway 21", "python",'2022-12-5'),
  (2, "kalyan", "Highway 20", "java",'2022-12-1'),
  (3, "salma", "ROADNO 32", "java",'2022-12-6'),
  (4, "ghouse", "KONDAPUR", ".net",'2022-10-11'),
  (5, "lokesh","madhapur", "frontend", '2022-11-14'),
  (6, "hari", "rtpp", "selenium",'2020-7-1'),
  (7,"manu","kadapa","django",'2021-9-20'),
  (8, "manoj","bangalore","sales",'2018-2-23')

]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")