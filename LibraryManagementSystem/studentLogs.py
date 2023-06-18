import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()

def insert_values(id,password,validity,status):
    sql=("insert into student(student_id,password,validity,status) values(%s,%s,%s,%s)")
    data=(id,password,validity,status)
    mycursor.execute(sql,data)
    mydb.commit()