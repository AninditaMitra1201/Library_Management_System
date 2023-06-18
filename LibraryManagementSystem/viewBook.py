import adminLoginMenu
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored

def view_books(id):
    print(colored("Sl No.    Book ID    Available Qty  Taken Qty    Created By   Created At                Book Name        Book Category",'red','on_white'))
    sql=("select id,book_id,available_qty,taken_qty,created_by,created_at,book_name,book_cat from book_mas")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            print(j,end='|        ')
        print()
    adminLoginMenu.adminloginmenu(id)
