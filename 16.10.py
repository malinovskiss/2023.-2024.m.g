import mysql.connector

db = mysql.connector.connect(host= 'localhost',database='biblioteka',user='root',password='Igars000')
print(db)

cursor = db.cursor()

sql = ("""
insert into dakteris (lasitajs, gramatas, autors)
values (%s,%s,%s,%s);
        """)

data = (1,"Edgars","Malinovskis","23657739")
cursor.execute(sql,data)
db.commit()
db.close()
