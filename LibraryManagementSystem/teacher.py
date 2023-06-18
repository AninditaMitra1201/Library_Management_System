from termcolor import colored
import mainMenu
import teacherSignUp
import teacherLogin

def mainmenu():
    print(colored("-----------------------------",'green'))
    print(colored("WELCOME TO TEACHER PANEL",'green'))
    print(colored("-----------------------------",'green'))
    print(colored("1. PRESS 1 TO LOG IN.",'yellow'))
    print(colored("2. PRESS 2 TO SIGN UP.",'yellow'))
    print(colored("3. PRESS 3 TO RETURN TO MAIN MENU.",'yellow'))
    usch=int(input(colored("Enter Your Choice : ",'yellow')))
    teacher_input(usch)
    
def teacher_input(usch):
    if(usch==1):
        teacherLogin.login()
    elif(usch==2):
        teacherSignUp.signup()
    elif(usch==3):
        mainMenu.mainmenu()
    else:
        print(colored("Invalid Input.",'red'))

