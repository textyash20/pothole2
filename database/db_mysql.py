import mysql.connector

name = int(input("ENTER name:  "))
uid = int(input("enter uid:    "))

print(type(name))
print(type(uid))

try:
    conn = mysql.connector.connect(host="85.10.205.173", username="yash_admin", password="12345678",
                                   database="potholebyyash")
    print("connection succefullllly")
except:
    print("not connected")

try:
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO 'test'('name','uid') VALUES('{}','{}') """.format(name, uid))
    conn.commit()
    print("commidted")

except:
    print("not commited")
