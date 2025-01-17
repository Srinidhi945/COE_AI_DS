import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)
mycursor=mydb.cursor()
q="create table employee(eid int(20) primary key,ename varchar(20),esal float(10));"
mycursor.execute(q)
mydb.commit()