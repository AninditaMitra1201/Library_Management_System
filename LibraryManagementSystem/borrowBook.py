import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored
from datetime import date,timedelta
import datetime
import studentLoginMenu
import teacherLoginMenu

def borrowing_eligibility(id1,bid):
    if(bid=='s'):
        id=[]
        id.append(id1)
        count=0
        sql=("select count(book_name) from book_log where borrower_id=%s and status='BORROWED'")
        data=(id)
        mycursor.execute(sql,data)
        for i in mycursor:
            for j in i:
                count=j
        print("Count = ",count)
        if(count>=3):
            return 0
        elif(count<3):
            return 1
    elif(bid=='t'):
        return 1



def choice_menu(id1):
    id=[]
    id.append(id1)
    flag=0
    while(flag==0):
        sql=("select distinct book_cat from book_mas")
        mycursor.execute(sql)
        li=[]
        for i in mycursor:
            for j in i:
                li.append(j)
        for i in range(len(li)):
            print(f"PRESS {i+1} for {li[i]}")
        ch=int(input(colored("Enter Here : ",'cyan')))
        if(ch>len(li) or ch<=0):
            print(colored("Invalid Input.",'red'))
            continue
        else:
            c=li[ch-1]
            flag=1
            break
    return c
            
def eligibility_of_category(id1,bid,c):
    if(bid=='s'):
        id=[]
        id.append(id1)
        sql=("select book_mas.book_cat from book_mas,book_log where book_mas.book_id=book_log.book_id and book_log.borrower_id=%s and status='BORROWED'")
        data=(id)
        mycursor.execute(sql,data)
        cate=[]
        for i in mycursor:
            for j in i:
                cate.append(j)
        #print(cate)
        if(c in cate):
            print(colored("You cannot borrow more than one book from a category.",'red'))
            return 0
        else:
            return 1
    elif(bid=='t'):
        return 1



def display_books(cat):
    flag=0
    while(flag==0):
        sql=("select book_name from book_mas where book_cat=%s")
        category=[]
        category.append(cat)
        data=(category)
        booknames=[]
        mycursor.execute(sql,data)
        for i in mycursor:
            for j in i:
                booknames.append(j)
        for i in range(len(booknames)):
            print(f"PRESS {i+1} for {booknames[i]}")
        ch=int(input(colored("Enter Here : ",'cyan')))
        if(ch>len(booknames) or ch<=0):
            print(colored("Invalid Input.",'red'))
            continue
        else:
            ch_book=booknames[ch-1]
        return ch_book
    
def availability(ch_book):
        sql=("select available_qty from book_mas where book_name=%s")
        bkname=[]
        bkname.append(ch_book)
        data=(bkname) 
        mycursor.execute(sql,data)
        for i in mycursor:
            for j in i:
                if(j==0):
                    print(colored("BOOK OUT OF STOCK!",'red'))
                    return 0
                else:
                    return j

def borrowLogUpdate(ch_book,id,bid):
    bkna=[]
    bkna.append(ch_book)
    sql=("select available_qty from book_mas where book_name=%s")
    data=(bkna)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            j=j-1
            sql=("update book_mas set available_qty=%s where book_name=%s")
            data=(j,ch_book)
            mycursor.execute(sql,data)
    sql=("select taken_qty from book_mas where book_name=%s")
    data=(bkna)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            j=j+1
            sql=("update book_mas set taken_qty=%s where book_name=%s")
            data=(j,ch_book)
            mycursor.execute(sql,data)
    sql=("select book_id from book_mas where book_name=%s")
    data=(bkna)
    mycursor.execute(sql,data)
    for i in mycursor:
        for j in i:
            book_id=j
    status='BORROWED'
    now=date.today()
    now1=datetime.datetime.now()
    current_time=now1.strftime("%H:%M:%S")
    due_date=now+timedelta(days=15)
    if(bid=='s'):
        sql=("insert into book_log(book_id,book_name,borrower_id,status,issued_on,issued_at,due_date) values(%s,%s,%s,%s,%s,%s,%s)")
        data=(book_id,ch_book,id,status,now,current_time,due_date)
        mycursor.execute(sql,data)
        #mydb.commit()
    elif(bid=='t'):
        sql=("insert into book_log(book_id,book_name,borrower_id,status,issued_on,issued_at) values(%s,%s,%s,%s,%s,%s)")
        data=(book_id,ch_book,id,status,now,current_time)
        mycursor.execute(sql,data)
        #mydb.commit()
    mydb.commit()
    print("BOOK ISSUED TO : ",id)
    if(bid=='s'):
        studentLoginMenu.studentloginmenu(id)
    elif(bid=='t'):
        teacherLoginMenu.teacherloginmenu(id)
    


def borrow_book(id,bid):
    flag=0
    while(flag==0):
        eli=borrowing_eligibility(id,bid)
        if(eli==1):
            print(colored("BOOK BORROWING CORNER",'cyan'))
            cat=choice_menu(id)
            eli_cat=eligibility_of_category(id,bid,cat)
            if(eli_cat==1):
                ch_book=display_books(cat)
                qty=availability(ch_book)
                if(qty==0):
                    continue
                else:
                    borrowLogUpdate(ch_book,id,bid)
                    break
            elif(eli_cat==0):
                continue
        elif(eli==0):
            print(colored("You cannot borrow more than three books.",'red'))
            if(bid=='s'):
                studentLoginMenu.studentloginmenu(id)
            elif(bid=='t'):
                teacherLoginMenu.teacherloginmenu(id)


# id='EE/2020/044'
# bid='s'
# c='JAVA'
# borrow_book(id,bid)
# #ch=eligibility_of_category(id,bid,c)
# #print(ch)
