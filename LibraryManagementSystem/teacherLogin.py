import mysql.connector
import teacher
from termcolor import colored
import teacherLoginMenu
import utilities

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
mydb2=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='Master')
mycursor2=mydb2.cursor()

def fetch_id_pwd():
    id,pwd=[],[]
    id_pwd={}
    sql=("select teacher_id from teacher")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            id.append(j)
    sql=("select password from teacher")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            pwd.append(j)
    id_pwd=dict(zip(id,pwd))
    return id_pwd

def fetch_id_status():
    id,status=[],[]
    id_status={}
    sql=("select teacher_id from teacher")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            id.append(j)
    sql=("select status from teacher")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            status.append(j)
    id_status=dict(zip(id,status))
    return id_status

def login():
    false=0
    c,i=1,1
    id_pwd=fetch_id_pwd()
    id_status=fetch_id_status()
    print(colored("Log In to your account.",'yellow'))
    id=input(colored("Enter your Teacher ID : ",'green'))
    #print(id_status.get(id))
    if(id_status.get(id)==0):
        print(colored("This account is blocked.",'red'))
    elif(id in id_pwd.keys() and id_status[id]==1):
        print(colored("Press 1 to Enter Password.",'grey'))
        print(colored("Forgot Password? Press 2 to Reset.",'grey'))
        choice=int(input(colored("Enter Here : ",'green')))
        if(choice==1):
            while(c<=3):
                pwd=input(colored("Enter Password : ",'green'))
                if(pwd==id_pwd[id]):
                    print('Logged In to : ',id)
                    teacherLoginMenu.teacherloginmenu(id)
                    break
                elif(pwd!=id_pwd[id]):
                    if(i<=2):
                        print(colored("Incorrect Password. Try Again.",'red'))
                        i=i+1
                    c=c+1
            if(c>3):
                print(colored("You have entered password incorrectly for 3 times. This Teacher Account is now BLOCKED.",'red'))
                sql=("update teacher set status=%s where teacher_id=%s")
                data=(false,id)
                mycursor.execute(sql,data)
                mydb.commit()
        elif(choice==2):
            sql=("select email from tea_mas where teacher_id=%s")
            st_id=[]
            st_id.append(id)
            data=(st_id)
            mycursor2.execute(sql,data)
            em=[]
            for i in mycursor2:
                for j in i:
                    em.append(j)
            ch=utilities.verify_email(em)
            if(ch!=0):
                new_pwd=utilities.input_password()
                sql=("update teacher set password=%s where teacher_id=%s")
                data=(new_pwd,id)
                mycursor.execute(sql,data)
                print(colored("New Password Set.",'green'))
                mydb.commit()
            elif(ch==0):
                teacher.mainmenu()
        else:
            print(colored("Invalid Input.",'red'))
            teacher.mainmenu()
    else:
        print(colored("Teacher ID does not exist.",'red'))
    teacher.mainmenu()
