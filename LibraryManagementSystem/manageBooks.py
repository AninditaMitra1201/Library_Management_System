import createBook
import editBook
import removeBook
import viewBook
from termcolor import colored

def manage_books(id):
    print(colored("-----MANAGE BOOKS-----",'cyan'))
    print(colored("PRESS 1 TO ADD A BOOK",'magenta'))
    print(colored("PRESS 2 TO EDIT A BOOK",'magenta'))
    print(colored("PRESS 3 TO REMOVE A BOOK",'magenta'))
    print(colored("PRESS 4 TO VIEW BOOKS",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    user_ch(ch,id)

def user_ch(ch,id):
    flag=0
    while(flag==0):
        if(ch==1):
            createBook.create_book(id)
        elif(ch==2):
            editBook.edit_book(id)
        elif(ch==3):
            removeBook.remove_book(id)
        elif(ch==4):
            viewBook.view_books(id)
        else:
            print(colored("INAVLID INPUT",'red'))
            break