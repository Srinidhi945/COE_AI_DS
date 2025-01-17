import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)

mycursor = mydb.cursor()
name=input("enter your name:")
id=int(input("enter employee id:"))
sal=float(input("enter your salary:"))
print("1.update name\n2.update salary\n")
op=int(input("choose your option:"))
if(op==1):
    mycursor.execute("UPDATE employee SET ename=%s WHERE eid=%s",(name,id))
    mydb.commit()
elif(op==2):
    mycursor.execute("UPDATE employee SET esal=%s WHERE eid=%s", (sal, id))
    mydb.commit()



