import mysql.connector
import sys
sys.path.append("LibraryManagementSystem")
import utilities
from termcolor import colored

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='Master')
mycursor=mydb.cursor()

def input_roll():
    flag=0
    while(flag==0):
        roll=(input(colored("Enter your Roll Number : ",'green')))
        if(len(roll)>=1 and len(roll)<=3):
            return roll
        else:
            print(colored("Incorrect Roll Number.",'red'))
            flag==0

def input_blood():
    blood=(input(colored("Enter your Blood Group : ",'green')))
    return blood

def input_trade():
    trade=(input(colored("Enter your Trade : ",'green')))
    return trade.upper()

def year_of_admission():
    yoa=int(input(colored("Enter your Year of Admission : ",'green')))
    return yoa

def year_of_passout():
    yop=int(input(colored("Enter your Year of Passout : ",'green')))
    return yop

def parent_name():
    parent_name=(input(colored("Enter your Parent's name : ",'green')))
    return parent_name.upper()

def parent_phone():
    flag=0
    while(flag==0):
        phone=input(colored("Enter your Parent's phone number : ",'green'))
        if(len(phone)==10 and phone.isnumeric()):
            return phone
        else:
            print(colored("Invalid Phone Number. Try Again.",'red'))
            flag==0

def address():
    adr=input(colored("Enter your address : ",'green'))
    return adr

def generate_student_id(trade,yoa,roll):
    if(len(roll)==1):
        stud_id=trade+'/'+str(yoa)+'/'+'00'+roll
    elif(len(roll)==2):
        stud_id=trade+'/'+str(yoa)+'/'+'0'+roll
    elif(len(roll)==3):
        stud_id=trade+'/'+str(yoa)+'/'+roll
    print("Your Student ID is : ",stud_id)
    return stud_id

def student_details():
    flag=0
    while(flag==0):
        fname=utilities.input_fname()
        lname=utilities.input_lname()
        adr=address()
        li=[]
        sql=("select email from stud_mas")
        mycursor.execute(sql)
        for i in mycursor:
            for j in i:
                li.append(j)
        email=utilities.check_email(li)
        mail=utilities.verify_email(email)
        if(mail!=0):
            phone=utilities.check_phone()
            password=utilities.input_password()
            roll=input_roll()
            blood=input_blood()
            trade=input_trade()
            yoa=year_of_admission()
            yop=year_of_passout()
            parname=parent_name()
            parph=parent_phone()
            stud_id=generate_student_id(trade,yoa,roll)
            #print(fname,lname,email,phone,password,roll,blood,trade,yoa,yop,parname,parph,stud_id)
            insert_data(stud_id,password,fname,lname,adr,mail,phone,roll,blood,trade,yoa,yop,parname,parph)
        elif(mail==0):
            continue

def insert_data(stud_id,password,fname,lname,adr,email,phone,roll,blood,trade,yoa,yop,parname,parph):
    sql=("insert into stud_mas values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data=(stud_id,password,fname,lname,adr,email,phone,roll,blood,trade,yoa,yop,parname,parph)
    mycursor.execute(sql,data)
    mydb.commit()


student_details()