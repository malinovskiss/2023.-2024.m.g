import mysql.connector

db = mysql.connector.connect(host= 'localhost',database='biblioteka',user='root',password='Igars000')
print(db)

cursor= db.cursor()

sql = ("""
insert.into biblioteka (lasitajs, gramatas, autors)
values (%s,%s,%s,%s);
""")
dati = (564,"Ģramatas nosaukums")
db.commit
