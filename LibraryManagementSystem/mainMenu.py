import admin
import student
import teacher
from termcolor import colored

def mainmenu():
    print(colored("-----------------------------",'grey'))
    print(colored("  WELCOME TO ONLINE LIBRARY",'blue'))
    print(colored("-----------------------------",'grey'))
    print(colored("1. PRESS 1 FOR ADMIN.",'magenta'))
    print(colored("2. PRESS 2 FOR STUDENT.",'magenta'))
    print(colored("3. PRESS 3 FOR TEACHER.",'magenta'))
    print(colored("4. PRESS 4 TO EXIT.",'magenta'))
    user_ch=int(input(colored("ENTER HERE : ",'grey')))
    userinput(user_ch)

def userinput(user_ch):
    if (user_ch==1):
        admin.mainmenu()
    elif(user_ch==2):
        student.mainmenu()
    elif(user_ch==3):
        teacher.mainmenu()
    elif (user_ch==4):
        print(colored("~~~~~~~~~~~~~~~~~~~~~~~",'cyan'))
        print(colored("Thank You for Visiting.",'grey'))
        print(colored("~~~~~~~~~~~~~~~~~~~~~~~",'cyan'))
        exit(0)
        