import mysql.connector


def update_people(id,name):
    mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="roottoor",
       database="nithya_ece1"
    )
    print("connected database sucessfully.")

    mycursor = mydb.cursor()
    sql = "update people SET name = %lavanya  WHERE id = %5"
    val = [id,name]
    mycursor.execute(sql,val)

    mydb.comit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount, "record inserted")


id = input("enter the id")
name = input("enter the name")
update_people(id,name)
