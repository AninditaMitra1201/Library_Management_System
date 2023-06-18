import adminLoginMenu
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored

def get_bk_id():
    flag=0
    while(flag==0):
        bkid=input(colored("Enter the Book ID : ",'cyan'))
        sql=("select book_id from book_mas")
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
    


def editCat(id):
    bk_id=get_bk_id()
    bk=[]
    bk.append(bk_id)
    sql=("select book_cat from book_mas where book_id=%s")
    data=(bk)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            print("Current category of the book is : ",j)
    cat=input(colored("Enter new book category : ",'cyan'))
    cat=cat.upper()
    sql=("update book_mas set book_cat=%s where book_id=%s")
    data=(cat,bk_id)
    mycursor.execute(sql,data)
    mydb.commit()
    print(colored("Book Category Updated",'green'))
    adminLoginMenu.adminloginmenu(id)

def editName(id):
    bk_id=get_bk_id()
    bk=[]
    bk.append(bk_id)
    sql=("select book_name from book_mas where book_id=%s")
    data=(bk)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            print("Current name of the book is : ",j)
    name=input(colored("Enter new book name : ",'cyan'))
    name=name.upper()
    sql=("update book_mas set book_name=%s where book_id=%s")
    data=(name,bk_id)
    mycursor.execute(sql,data)
    mydb.commit()
    print(colored("Book Name Updated",'green'))
    adminLoginMenu.adminloginmenu(id)

def editQty(id):
    bk_id=get_bk_id()
    bk=[]
    bk.append(bk_id)
    sql=("select available_qty from book_mas where book_id=%s")
    data=(bk)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            print("Current available quantity of the book is : ",j)
    qty=int(input(colored("Enter new book quantity : ",'cyan')))
    sql=("update book_mas set available_qty=%s where book_id=%s")
    data=(qty,bk_id)
    mycursor.execute(sql,data)
    mydb.commit()
    print(colored("Book Quantity Updated",'green'))
    adminLoginMenu.adminloginmenu(id)


def edit_book(id):
    print(colored("PRESS 1 TO EDIT BOOK CATEGORY",'magenta'))
    print(colored("PRESS 2 TO EDIT BOOK NAME",'magenta'))
    print(colored("PRESS 3 TO EDIT BOOK QUANTITY",'magenta'))  
    ch=int(input(colored("Enter Here : ",'cyan')))
    user_ch(ch,id) 


def user_ch(ch,id):
    flag=0
    while(flag==0):
        if(ch==1):
            editCat(id)
        elif(ch==2):
            editName(id)
        elif(ch==3):
            editQty(id)
        else:
            print(colored("INAVLID INPUT",'red'))
            break
