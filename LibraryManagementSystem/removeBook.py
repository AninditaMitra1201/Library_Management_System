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

def remove_book(id):
    bkid=get_bk_id()
    bk_id=[]
    bk_id.append(bkid)
    sql=(" delete from book_mas where book_id=%s")
    data=(bk_id)
    mycursor.execute(sql,data)
    mydb.commit()
    print(colored("BOOK REMOVED SUCCESSFULLY",'green'))
    adminLoginMenu.adminloginmenu(id)