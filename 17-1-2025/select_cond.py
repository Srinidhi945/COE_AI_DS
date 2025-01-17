import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="67b4_coe"
)

mycursor = mydb.cursor()

eid = input("Enter employee ID: ")

q = f"SELECT * FROM employee WHERE eid = {eid};"

mycursor.execute(q)

result = mycursor.fetchall()

for row in result:
    print(row)

mydb.close()
