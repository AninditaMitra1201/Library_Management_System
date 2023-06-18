import mysql.connector
import studentLoginMenu
import teacherLoginMenu
from datetime import date
import datetime
#import returnBookLogUpdate
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored

def check_bid(id,bid):
    if(bid=='s'):
        studentLoginMenu.studentloginmenu(id)
    elif(bid=='t'):
        teacherLoginMenu.teacherloginmenu(id)

def check_if_id_has_borrowed_book(id):
    sql=("select distinct borrower_id from book_log where status='BORROWED'")
    mycursor.execute(sql)
    li=[]
    for i in mycursor:
        for j in i:
            li.append(j)
    if(id in li):
        print(colored("BOOK RETURNING CORNER",'cyan'))
        return 1
    else:
        print(colored("You have no books to return.",'red'))
        return 0

def check_if_book_available_to_return(id,bid):
    li=[]
    li.append(id)
    sql=("select distinct book_name from book_log where borrower_id=%s and status='BORROWED'")
    data=(li)
    mycursor.execute(sql,data)
    book_name=[]
    for i in mycursor:
        for j in i:
            book_name.append(j)
    if(len(book_name)==0):
        print(colored("You have returned all books.",'green'))
        check_bid(id,bid)
    else:
        return book_name


def choice_menu_of_borrowed_books(book_name):
    flag=0
    while(flag==0):
        for i in range(len(book_name)):
            print(f"PRESS {i+1} to return {book_name[i]}")
        ch=int(input(colored("Enter Here : ",'cyan')))
        if(ch>len(book_name) or ch<=0):
            print(colored("Invalid Input.",'red'))
            continue
        else:
            ch_book=book_name[ch-1]
        print(ch_book)
        return ch_book

def return_selected_book(id,ch_book,bid):
    sql=("update book_log set status='RETURNED' where borrower_id=%s and book_name=%s")
    data=(id,ch_book)
    mycursor.execute(sql,data)
    mydb.commit()
    now=date.today()
    now1=datetime.datetime.now()
    current_time=now1.strftime("%H:%M:%S")
    sql=("update book_log set returned_on=%s,returned_at=%s where borrower_id=%s and book_name=%s")
    data=(now,current_time,id,ch_book)
    mycursor.execute(sql,data)
    bkna=[]
    bkna.append(ch_book)
    sql=("select available_qty from book_mas where book_name=%s")
    data=(bkna)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            j=j+1
            sql=("update book_mas set available_qty=%s where book_name=%s")
            data=(j,ch_book)
            mycursor.execute(sql,data)
    sql=("select taken_qty from book_mas where book_name=%s")
    data=(bkna)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            j=j-1
            sql=("update book_mas set taken_qty=%s where book_name=%s")
            data=(j,ch_book)
            mycursor.execute(sql,data)
    print(colored("BOOK RETURNED.",'green'))
    mydb.commit()
    check_bid(id,bid)


def return_book(id,bid):
    flag=0
    while(flag==0):
        ret=check_if_id_has_borrowed_book(id)
        if(ret==1):
            book_name=check_if_book_available_to_return(id,bid)
            ch_book=choice_menu_of_borrowed_books(book_name)
            return_selected_book(id,ch_book,bid)
        elif(ret==0):
            check_bid(id,bid)
