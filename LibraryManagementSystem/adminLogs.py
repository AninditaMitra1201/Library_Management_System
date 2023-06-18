import datetime
from termcolor import colored
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
def insert_values(fname,lname,email,phone,password,admin_id):
    #print(fname,lname,admin_id,password,phone,email)
    true=1
    status=true
    now=datetime.datetime.now()
    sql=("insert into admin(admin_id,email_id,password,phone,first_name,last_name,status,time_stamp) values(%s,%s,%s,%s,%s,%s,%s,%s)")
    data=(admin_id,email,password,phone,fname,lname,status,now)
    mycursor.execute(sql,data)
    mydb.commit()
