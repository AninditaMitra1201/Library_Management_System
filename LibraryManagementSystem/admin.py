import mainMenu
import adminSignUp
import adminLogin
from termcolor import colored
def mainmenu():
    print(colored("-----------------------------",'green'))
    print(colored("  WELCOME TO ADMIN PANEL",'green'))
    print(colored("-----------------------------",'green'))
    print(colored("1. Existing User? LOG IN.",'yellow'))
    print(colored("2. New User? SIGN UP.",'yellow'))
    print(colored("3. PRESS 3 TO RETURN TO MAIN MENU.",'yellow'))
    ad_ch=int(input(colored("ENTER HERE : ",'green')))
    admininput(ad_ch)
def admininput(ad_ch):
    if(ad_ch==1):
        adminLogin.login()
    elif(ad_ch==2):
        adminSignUp.signup()
    elif(ad_ch==3):
        mainMenu.mainmenu()
    else:
        print(colored("INVALID INPUT",'red'))