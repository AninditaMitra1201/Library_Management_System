import csv
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored
import adminLoginMenu

def get_bk_id():
    flag=0
    while(flag==0):
        bkid=input(colored("Enter the Book ID : ",'cyan'))
        sql=("select book_id from book_log")
        mycursor.execute(sql)
        bk=[]
        for i in mycursor:
            for j in i:
                bk.append(j)
        if(bkid in bk):
            return bkid
        else:
            print(colored("BOOK ID does not exist.",'red'))
            continue

def get_user_id(bid):
    if(bid=='s'):
        flag=0
        while(flag==0):
            bkid=input(colored("Enter the Student ID : ",'cyan'))
            sql=("select distinct borrower_id from book_log")
            mycursor.execute(sql)
            bk=[]
            for i in mycursor:
                for j in i:
                    bk.append(j)
            if(bkid in bk):
                return bkid
            else:
                print(colored("Student ID does not exist.",'red'))
                continue
    elif(bid=='t'):
        flag=0
        while(flag==0):
            bkid=input(colored("Enter the Teacher ID : ",'cyan'))
            sql=("select distinct borrower_id from book_log")
            mycursor.execute(sql)
            bk=[]
            for i in mycursor:
                for j in i:
                    bk.append(j)
            if(bkid in bk):
                return bkid
            else:
                print(colored("Teacher ID does not exist.",'red'))
                continue

def by_bk_id(id):
    bkid=get_bk_id()
    sql=("select * from book_log where book_id=%s")
    bk_id=[]
    bk_id.append(bkid)
    data=(bk_id)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            print(j,end=' ')
        print()
    adminLoginMenu.adminloginmenu(id)

def by_u_id(id,bid):
    uid=get_user_id(bid)
    if(bid=='s'):
        sql=("select * from book_log where borrower_id=%s")
        u_id=[]
        u_id.append(uid)
        data=(u_id)
        mycursor.execute(sql,data)
    elif(bid=='t'):
        sql=("select book_id,book_name,status,issued_on,issued_at,returned_on,returned_at from book_log where borrower_id=%s")
        u_id=[]
        u_id.append(uid)
        data=(u_id)
        mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            print(j,end=' ')
        print()
    adminLoginMenu.adminloginmenu(id)

def download_csv(id):
    sql=("select * from book_log")
    mycursor.execute(sql)
    li=[]
    for i in mycursor:
            li.append(i)
    cn=[]
    sql=("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'book_log' order by ordinal_position asc")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            cn.append(j)
    li.insert(0,tuple(cn))
    with open('C:/Users/ANINDITA/Documents/Python/LibraryManagementSystem/booklogs/Book Logs .csv','w') as f:
        writer=csv.writer(f)
        writer.writerows(li)
    print(colored("BOOK LOG DOWNLOADED AS CSV",'green'))
    adminLoginMenu.adminloginmenu(id)


def userch(ch,id):
    flag=0
    while(flag==0):
        if(ch==1):
            by_bk_id(id)
        elif(ch==2):
            bid='s'
            by_u_id(id,bid)
        elif(ch==3):
            bid='t'
            by_u_id(id,bid)
        if(ch==4):
            download_csv(id)
        else:
            print(colored("INVALID INPUT",'red'))
            break

def book_details(id):
    print(colored("PRESS 1 TO VIEW BOOK DETAILS BY BOOK ID",'cyan'))
    print(colored("PRESS 2 TO VIEW BOOK DETAILS BY STUDENT ID",'cyan'))
    print(colored("PRESS 3 TO VIEW BOOK DETAILS BY TEACHER ID",'cyan'))
    print(colored("PRESS 4 TO DOWNLOAD BOOK LOG AS CSV FILE",'cyan'))
    ch=int(input(colored("Enter here : ",'magenta')))
    userch(ch,id)
