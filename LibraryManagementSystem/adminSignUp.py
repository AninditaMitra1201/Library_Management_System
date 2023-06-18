from termcolor import colored
import adminLogs
import utilities
import admin
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database="LibraryManagementSystem")
mycursor=mydb.cursor()

def generate_admin_id():
    admin_id,j="",""
    sql=("select auto_increment from information_schema.tables where table_name='admin'")
    mycursor.execute(sql)
    for i in mycursor:
        for k in i:
            j=str(k)
            if(len(j)==1):
                admin_id='AD'+'00'+j
            elif(len(j)==2):
                admin_id='AD'+'0'+j
            else:
                admin_id='AD'+j
    print("Your Admin ID is : ",admin_id)
    return admin_id
    
def signup():
    print(colored("Sign-Up to create an account.",'yellow'))
    fname=utilities.input_fname()
    lname=utilities.input_lname()
    li=[]
    sql=("select email_id from admin")
    mycursor.execute(sql)
    for i in mycursor:
        for j in i:
            li.append(j)
    email=utilities.check_email(li)
    mail=utilities.verify_email(email)
    if(mail!=0):
        phone=utilities.check_phone()
        password=utilities.input_password()
        admin_id=generate_admin_id()
        adminLogs.insert_values(fname,lname,mail,phone,password,admin_id)
        print(colored("Account Created Successfully. ",'green'))
        admin.mainmenu()
    elif(mail==0):
        admin.mainmenu()