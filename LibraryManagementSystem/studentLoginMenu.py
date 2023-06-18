from termcolor import colored
import student
import borrowBook
import returnBook

def studentloginmenu(id):
    #print("Logged in to : ",id)
    print(colored("PRESS 1 TO BORROW BOOKS",'magenta'))
    print(colored("PRESS 2 TO RETURN BOOKS",'magenta'))
    print(colored("PRESS 3 TO RETURN TO STUDENT PANEL",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    userinput(ch,id)

def userinput(ch,id):
    bid='s'
    flag=0
    while(flag==0):
        if(ch==1):
            borrowBook.borrow_book(id,bid)
        elif(ch==2):
            returnBook.return_book(id,bid)
        elif(ch==3):
            student.mainmenu()
        else:
            print(colored("INVALID INPUT.",'red'))
            break
    