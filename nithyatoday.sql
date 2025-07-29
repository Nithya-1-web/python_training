mycursor = mydb.cursor()

sql = "INSERT INTO user1(id,name,email"
"values(%s,%s,%s)"
val = (id,name,email)
mycursor.execute(sql,val)


