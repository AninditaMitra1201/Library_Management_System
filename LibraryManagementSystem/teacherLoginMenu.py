from termcolor import colored
import teacher
import borrowBook
import returnBook

def teacherloginmenu(id ):
    #print("Logged in to : ",id)
    print(colored("PRESS 1 TO BORROW BOOKS",'magenta'))
    print(colored("PRESS 2 TO RETURN BOOKS",'magenta'))
    print(colored("PRESS 3 TO RETURN TO TEACHER PANEL",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    userinput(ch,id)

def userinput(ch,id):
    bid='t'
    flag=0
    while(flag==0):
        if(ch==1):
            borrowBook.borrow_book(id,bid)
        elif(ch==2):
            returnBook.return_book(id,bid)
        elif(ch==3):
            teacher.mainmenu()
        else:
            print(colored("INVALID INPUT.",'red'))
            break
    
