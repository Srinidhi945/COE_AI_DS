import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)
mycursor=mydb.cursor()
q="delete from employee where eid=2;"
mycursor.execute(q)
mydb.commit()