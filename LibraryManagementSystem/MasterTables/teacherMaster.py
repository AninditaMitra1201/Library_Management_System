import mysql.connector
import sys
sys.path.append("LibraryManagementSystem")
import utilities
from termcolor import colored

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database="Master")
mycursor=mydb.cursor()

def address():
    adr=input(colored("Enter your address : ",'green'))
    return adr

def input_blood():
    blood=(input(colored("Enter your Blood Group : ",'green')))
    return blood

def generate_teacher_id():
    teacher_id,j="",""
    sql=("select auto_increment from information_schema.tables where table_name='tea_mas'")
    mycursor.execute(sql)
    for i in mycursor:
        for k in i:
            j=str(k)
            if(len(j)==1):
                teacher_id='TE'+'00'+j
            elif(len(j)==2):
                teacher_id='TE'+'0'+j
            else:
                teacher_id='TE'+j
    print("Your Teacher ID is : ",teacher_id)
    return teacher_id

def teacher_details():
    flag=0
    while(flag==0):
        fname=utilities.input_fname()
        lname=utilities.input_lname()
        adr=address()
        li=[]
        sql=("select email from tea_mas")
        mycursor.execute(sql)
        for i in mycursor:
            for j in i:
                li.append(j)
        email=utilities.check_email(li)
        mail=utilities.verify_email(email)
        if(mail!=0):
            phone=utilities.check_phone()
            password=utilities.input_password()
            blood=input_blood()
            tea_id=generate_teacher_id()
            insert_data(tea_id,fname,lname,adr,mail,phone,password,blood)
        elif(mail==0):
            continue

def insert_data(tea_id,fname,lname,address,email,phone,password,blood):
    sql=("insert into tea_mas(teacher_id,fname,lname,address,email,phone,password,blood) values(%s,%s,%s,%s,%s,%s,%s,%s)")
    data=(tea_id,fname,lname,address,email,phone,password,blood)
    mycursor.execute(sql,data)
    mydb.commit()

teacher_details()