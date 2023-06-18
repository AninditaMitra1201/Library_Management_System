import csv
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()


sql=("select * from book_log")
mycursor.execute(sql)
li=[]
for i in mycursor:
        li.append(i)
#print(li)
cn=[]
sql=("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'book_log' order by ordinal_position asc")
mycursor.execute(sql)
for i in mycursor:
    for j in i:
        cn.append(j)
#for i in li:
#print(cn)
li.insert(0,tuple(cn))
#print(li)


with open('C:/Users/ANINDITA/Documents/Python/LibraryManagementSystem/booklogs/Book Logs .csv','w') as f:
     writer=csv.writer(f)
     writer.writerows(li)