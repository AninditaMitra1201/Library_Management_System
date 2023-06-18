import calculateDue
import studentBlockUnblock
import teacherBlockUnblock
from termcolor import colored

def manage_accounts(id):
    print(colored("-----MANAGE ACCOUNTS-----",'cyan'))
    print(colored("PRESS 1 TO CALCULATE DUE AMOUNT",'magenta'))
    print(colored("PRESS 2 TO DEDUCT DUE AMOUNT",'magenta'))
    print(colored("PRESS 3 TO CLEAR DUE AMOUNT",'magenta'))
    print(colored("PRESS 4 TO BLOCK/UNBLOCK STUDENT ACCOUNTS",'magenta'))
    print(colored("PRESS 5 TO BLOCK/UNBLOCK TEACHER ACCOUNTS",'magenta'))
    ch=int(input(colored("Enter Here : ",'cyan')))
    user_ch(ch,id)

def user_ch(ch,id):
    flag=0
    while(flag==0):
        if(ch==1):
            calculateDue.calculate_due(id)
        elif(ch==2):
            calculateDue.deduct_due(id)
        elif(ch==3):
            calculateDue.clear_due(id)
        elif(ch==4):
            studentBlockUnblock.student_Block_Unblock(id)
        elif(ch==5):
            teacherBlockUnblock.teacher_Block_Unblock(id)
        else:
            print(colored("INAVLID INPUT",'red'))
            break