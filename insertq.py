import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)
mycursor=mydb.cursor()
id=int(input("enter employee id:"))
name=input("enter your name:")
sal=float(input("enter your salary:"))
mycursor.execute("insert into employee values(%s,%s,%s)",(id,name,sal))
mydb.commit()

