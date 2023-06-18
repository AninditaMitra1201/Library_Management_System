import mysql.connector
import utilities
import teacherLogs
import teacher
from termcolor import colored

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='Master')
mycursor=mydb.cursor()
mydb1=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor1=mydb1.cursor()

sql=("select teacher_id from tea_mas")  #importing the existing teacher ids from master table
mycursor.execute(sql)
tea_id=[]
for i in mycursor:
    for j in i:
        tea_id.append(j)

sql=("Select teacher_id from teacher")  #importing the existing teacher IDs from teacher table of lib management sys
mycursor1.execute(sql)
tid=[]
for i in mycursor1:
    for j in i:
        tid.append(j)

def signup():
    print(colored("Sign-Up to create an account.",'yellow'))
    flag=0
    while(flag==0):
        id=input(colored("Enter yor Teacher ID : ",'green'))
        if(id in tea_id): # CHECKING IF TEACHER ID EXISTS IN MASTER DATA
            if(id in tid):  #CHECKING IF THE STUDENT ID ALREADY EXISTS IN LIB DATA
                print(colored("This Teacher ID already has an account.",'red'))
                flag=0
            else:
                password=utilities.input_password()
                status=1
                break
        else:
            print(colored("Teacher ID does not exist.",'red'))
            flag=0
    teacherLogs.insert_values(id,password,status)
    teacher.mainmenu()

    

