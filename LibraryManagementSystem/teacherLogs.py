import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()

def insert_values(id,password,status):
    sql=("insert into teacher values(%s,%s,%s)")
    data=(id,password,status)
    mycursor.execute(sql,data)
    mydb.commit()