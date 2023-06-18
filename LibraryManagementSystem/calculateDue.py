import datetime
import adminLoginMenu
from datetime import date,timedelta
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored

def get_sid():
    flag=0
    while(flag==0):
        sid=input(colored("Enter the Student ID : ",'cyan'))
        mycursor.execute("select distinct student.student_id from student inner join book_log on student.student_id=book_log.borrower_id")
        st=[]
        for i in mycursor:
            for j in i:
                st.append(j)
        if(sid in st):
            return sid
        else:
            print(colored("Incorrect Student ID",'red'))
            continue

def get_details(sid):
    s_id=[]
    s_id.append(sid)
    sql=("select status,returned_on,due_date from book_log where borrower_id=%s and pay_stat='UNPAID'")
    data=(s_id)
    mycursor.execute(sql,data)
    dets=[]
    for i in mycursor:
        dets.append(i)
    if(len(dets)>0):
        return dets
    elif(len(dets)==0):
        return 0

def calculate_due(id):
    sid=get_sid()
    dets=get_details(sid)
    today=date.today()
    due,real_due=0,0
    if(dets!=0):
        for i in range (len(dets)):
            if(dets[i][0]=='BORROWED' and today>dets[i][2]):
                diff=today-dets[i][2]
                due=1*(diff.days)
            elif(dets[i][0]=='RETURNED' and dets[i][1]>dets[i][2]):
                diff=dets[i][1]-dets[i][2]
                due=1*(diff.days)
            else:
                due=0
            real_due=real_due+due
            sql=("update student set due=%s where student_id=%s")
            data=(real_due,sid)
            mycursor.execute(sql,data)
            print(sid,"HAS A DUE OF Rs.",real_due)
            mydb.commit()
    elif(dets==0):
        print(colored("STUDENT HAS NO DUE TO CALCULATE.",'green'))
    adminLoginMenu.adminloginmenu(id)

def deduct_due_choicemenu(id,sid):
    flag=0
    while(flag==0):
        s_id=[]
        s_id.append(sid)
        sql=("select book_name from book_log where borrower_id=%s and pay_stat='UNPAID'")
        data=(s_id)
        mycursor.execute(sql,data)
        li=[]
        for i in mycursor:
            for j in i:
                li.append(j)
        if(len(li)>0):
            for i in range(len(li)):
                print(f"PRESS {i+1} to deduct due of {li[i]}")
            ch=int(input(colored("Enter Here DUE : ",'cyan')))
            if(ch>len(li) or ch<=0):
                print(colored("Invalid Input.",'red'))
                continue
            else:
                c=li[ch-1]
                return c
        elif(len(li)==0):
            print(colored("STUDENT HAS ALREADY CLEARED DUE.",'green'))
            adminLoginMenu.adminloginmenu(id)

def deduct_due(id):
    sid=get_sid()
    s_id=[]
    s_id.append(sid)
    ch=deduct_due_choicemenu(id,sid)
    today=date.today()
    now1=datetime.datetime.now()
    current_time=now1.strftime("%H:%M:%S")
    sql=("select status,returned_on,due_date from book_log where borrower_id=%s and book_name=%s")
    data=(sid,ch)
    mycursor.execute(sql,data)
    dets=[]
    for i in mycursor:
        dets.append(i)
    if(dets[0][0]=='BORROWED' and today>dets[0][2]):
        diff=today-dets[0][2]
        due=1*(diff.days)
        sql=("select due from student where student_id=%s")
        data=(s_id)
        mycursor.execute(sql,data)
        for i in mycursor:
            for j in i:
                ex_due=j
        real_due=ex_due-due
        sql=("update student  set due=%s where student_id=%s")
        data=(real_due,sid)
        mycursor.execute(sql,data)
        sql=("update book_log  set status='RETURNED',pay_stat='PAID',returned_on=%s,returned_at=%s where borrower_id=%s and book_name=%s")
        data=(today,current_time,sid,ch)
        mycursor.execute(sql,data)
        print("DUE DEDUCTED SUCCESSFULLY FOR :",sid,"PREVIOUS DUE : ",ex_due,"UPDATED DUE : ",real_due)
        mydb.commit()
    elif(dets[0][0]=='RETURNED' and dets[0][1]>dets[0][2]):
        diff=dets[0][1]-dets[0][2]
        due=1*(diff.days)
        sql=("select due from student where student_id=%s")
        data=(s_id)
        mycursor.execute(sql,data)
        for i in mycursor:
            for j in i:
                ex_due=j
        real_due=ex_due-due
        sql=("update student set due=%s where student_id=%s")
        data=(real_due,sid)
        mycursor.execute(sql,data)
        sql=("update book_log set pay_stat='PAID' where borrower_id=%s and book_name=%s")
        data=(sid,ch)
        mycursor.execute(sql,data)
        print("DUE DEDUCTED SUCCESSFULLY FOR :",sid,"PREVIOUS DUE : ",ex_due,"UPDATED DUE : ",real_due)
        mydb.commit()
    else:
        print(colored("THIS BOOK IS NOT DUE YET.",'green'))
    adminLoginMenu.adminloginmenu(id)

def clear_due(id):
    sid=get_sid()
    s_id=[]
    s_id.append(sid)
    sql=("update student set due=0 where student_id=%s")
    data=(s_id)
    mycursor.execute(sql,data)
    sql=("update book_log set pay_stat='PAID' where borrower_id=%s")
    data=(s_id)
    mycursor.execute(sql,data)
    print("DUE CLEARED SUCCESSFULLY FOR :",sid)
    mydb.commit()
    adminLoginMenu.adminloginmenu(id)
