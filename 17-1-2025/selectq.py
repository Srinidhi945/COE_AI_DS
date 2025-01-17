import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)
mycursor=mydb.cursor()
q="select * from employee;"
mycursor.execute(q)
emps=mycursor.fetchall()
for e in emps:
    print(e)
mydb.commit()