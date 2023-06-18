import datetime 
from termcolor import colored
import adminLoginMenu
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()

def bookname(li):
    flag=0
    while(flag==0):
        bname=input("Enter Book Name : ")
        bname=bname.upper()
        if(bname in li):
            print(colored("This Book already exists.",'red'))
            flag=0
        else:
            return bname
    
def bookcat():
    bcat=input("Enter Book Category : ")
    return bcat.upper()

def bookqty():
    qty=int(input("Enter the number of books to be added : "))
    return qty

def book_id():
    book_id,j="",""
    sql=("select auto_increment from information_schema.tables where table_name='book_mas'")
    mycursor.execute(sql)
    for i in mycursor:
        for k in i:
            j=str(k)
            if(len(j)==1):
                book_id='BOOK'+'00'+j
            elif(len(j)==2):
                book_id='BOOK'+'0'+j
            else:
                book_id='BOOK'+j
    print("BOOK ID is : ",book_id)
    return book_id
    


def create_book(admin_id):
    li=[]
    sql=("select book_name from book_mas")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            li.append(j)
    bname=bookname(li)
    bcat=bookcat()
    qty=bookqty()
    now=datetime.datetime.now()
    bookid=book_id()
    print(colored("BOOK CREATED",'green'))
    insert_into_book_mas(bookid,bname,bcat,qty,admin_id,now)
    adminLoginMenu.adminloginmenu(admin_id)

def insert_into_book_mas(bookid,bname,bcat,qty,admin_id,now):
    sql=("insert into book_mas(book_id,book_name,book_cat,available_qty,created_by,created_at) values(%s,%s,%s,%s,%s,%s)")
    data=(bookid,bname,bcat,qty,admin_id,now)
    mycursor.execute(sql,data)
    mydb.commit()