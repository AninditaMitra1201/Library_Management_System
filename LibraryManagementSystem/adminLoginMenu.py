from termcolor import colored
import manageBooks
import manageAccounts
import admin
import bookDetails


def adminloginmenu(admin_id):
    print("Logged in to : ",admin_id)
    print(colored("PRESS 1 TO MANAGE BOOKS",'magenta'))
    print(colored("PRESS 2 TO MANAGE ACCOUNTS",'magenta'))
    print(colored("PRESS 3 TO VIEW BOOK DETAILS",'magenta'))
    print(colored("PRESS 4 TO RETURN TO ADMIN PANEL",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    userinput(ch,admin_id)

def userinput(ch,admin_id):
    flag=0
    while(flag==0):
        if(ch==1):
            manageBooks.manage_books(admin_id)
        elif(ch==2):
            manageAccounts.manage_accounts(admin_id)
        elif(ch==3):
            bookDetails.book_details(admin_id)
        elif(ch==4):
            admin.mainmenu()
        else:
            print(colored("Inavlid Input"))
            break
