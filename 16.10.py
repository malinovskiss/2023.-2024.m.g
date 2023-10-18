import mysql.connector

db = mysql.connector.connect(host= 'localhost',database='biblioteka',user='root',password='Igars000')
print(db)
