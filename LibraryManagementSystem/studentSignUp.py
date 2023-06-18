import mysql.connector
import utilities
import studentLogs
import student
from termcolor import colored

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='Master')
mycursor=mydb.cursor()
mydb1=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor1=mydb1.cursor()

sql=("select stud_id from stud_mas")  # importing the student id and year of passout from master table  (11-23)
mycursor.execute(sql)
stu_id,yop=[],[]
for i in mycursor:
    for j in i:
        stu_id.append(j)
sql=("select year_of_pass from stud_mas")
mycursor.execute(sql)
for i in mycursor:
    for j in i:
        yop.append(j)
id_yop={}
id_yop=dict(zip(stu_id,yop))

sql=("Select student_id from student")  #importing the existing student IDs from student table of lib management sys
mycursor1.execute(sql)
sid=[]
for i in mycursor1:
    for j in i:
        sid.append(j)

def valid(id):  # calculating validity date of library card
    validity="30/06/"+str(id_yop[id])
    return validity

def signup():
    print(colored("Sign-Up to create an account.",'yellow'))
    flag=0
    while(flag==0):
        id=input(colored("Enter yor Student ID : ",'green'))
        if(id in id_yop.keys()): # CHECKING IF STUDENT ID EXISTS IN MASTER DATA
            if(id in sid):  #CHECKING IF THE STUDENT ID ALREADY EXISTS IN LIB DATA
                print(colored("This Student ID already has an account.",'red'))
                flag=0
            else:
                password=utilities.input_password()
                validity=valid(id)
                status=1
                break
        else:
            print(colored("Student ID does not exist.",'red'))
            flag=0
    studentLogs.insert_values(id,password,validity,status)
    student.mainmenu()

