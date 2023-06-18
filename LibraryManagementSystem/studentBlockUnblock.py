import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='chickenleg',database='LibraryManagementSystem')
mycursor=mydb.cursor()
from termcolor import colored
import adminLoginMenu


def choicemenu(stat):
    flag=0
    while(flag==0):
        status=[]
        status.append(stat)
        sql=("select student_id from student where status=%s")
        data=(status)
        mycursor.execute(sql,data)
        accounts=[]
        for i in mycursor:
            for j in i:
                accounts.append(j)
        if(len(accounts)>0):
            for i in range(len(accounts)):
                print(f"PRESS {i+1} to select {accounts[i]}")
            ch=int(input(colored("Enter Here : ",'cyan')))
            if(ch>len(accounts) or ch<=0):
                print(colored("Invalid Input.",'red'))
                continue
            else:
                c=accounts[ch-1]
                flag=1
                return c
        elif(len(accounts)==0):
            print(colored("No accounts available for this function.",'red'))
            return 0



def block_students(id):
    ch=choicemenu(1)
    ch1=[]
    ch1.append(ch)
    if(ch!=0):
        sql=("update student set status=0 where student_id=%s")
        data=(ch1)
        mycursor.execute(sql,data)
        mydb.commit()
        print(colored("ACCOUNT BLOCKED SUCCESSFULLY.",'green'))
        adminLoginMenu.adminloginmenu(id)
    elif(ch==0):
        adminLoginMenu.adminloginmenu(id)

def unblock_students(id):
    ch=choicemenu(0)
    ch1=[]
    ch1.append(ch)
    if(ch!=0):
        sql=("update student set status=1 where student_id=%s")
        data=(ch1)
        mycursor.execute(sql,data)
        mydb.commit()
        print(colored("ACCOUNT UNBLOCKED SUCCESSFULLY.",'green'))
        adminLoginMenu.adminloginmenu(id)
    elif(ch==0):
        adminLoginMenu.adminloginmenu(id)
    

def student_Block_Unblock(id):
    print(colored("PRESS 1 TO BLOCK ACCOUNTS",'magenta'))
    print(colored("PRESS 2 TO UNBLOCK ACCOUNTS",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    user_ch(ch,id)

def user_ch(ch,id):
    flag=0
    while(flag==0):
        if(ch==1):
            block_students(id)
        elif(ch==2):
            unblock_students(id)
        else:
            print(colored("INAVLID INPUT",'red'))
            break