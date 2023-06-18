from termcolor import colored
import re
import random
import smtplib

def input_fname():
    fname=input(colored("Enter your First Name : ",'green'))
    return fname.upper()

def input_lname():
    lname=input(colored("Enter your Last Name : ",'green'))
    return lname.upper()

def verify_email(mail):
    s=smtplib.SMTP('smtp.gmail.com',587) #creates smtp session
    s.starttls()  #start tls(transport layer security)
    s.login("mitra.anindita246@gmail.com","blcprgfednganjcr")
    num=random.randint(100000,999999)
    otp=str(num)
    message="Welcome to Anindita's Online Library. Your OTP is "+otp
    s.sendmail("mitra.anindita246@gmail.com",mail,message)
    print(colored("E-Mail Sent to your E-Mail ID.",'cyan'))
    verotp=input(colored("Enter the OTP : ",'cyan'))
    print(colored("Verifying....",'green'))
    if(verotp==otp):
        print(colored("Email ID Verified.",'green'))
        s.quit()
        return mail
    else:
        print(colored("Incorrect OTP",'red'))
        return 0
    


def check_email(li):
    flag=0
    while(flag==0):
        email=input(colored("Enter your E-mail ID : ",'green'))
        regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if(re.search(regex,email)):
            if(email in li):
                    print(colored("This E-mail id is already registered. Try another.",'red'))
                    flag=0
            else:
                return email
        else:
            print(colored("Invalid Email-ID. Try Again.",'red'))
            flag=0

def check_phone():
    flag=0
    while(flag==0):
        phone=input(colored("Enter your phone number : ",'green'))
        if(len(phone)==10 and phone.isnumeric()):
            return phone
        else:
            print(colored("Invalid Phone Number. Try Again.",'red'))
            flag==0

def suggest_password():
    sugg=""
    spcl=['@','#','$','%','*','&','%']
    num=[chr(i) for i in range (48,58)]
    small=[chr(i) for i in range(97,123)]
    caps=[chr(i) for i in range(65,91)]
    p1=random.choices(spcl,k=2)
    p2=random.choices(num,k=2)
    p3=random.choices(caps,k=2)
    p4=random.choices(small,k=2)
    su_pwd=p1+p2+p3+p4
    random.shuffle(su_pwd)
    for i in su_pwd:
        sugg=sugg+i
    return sugg

def check_password():
    flag=0
    while(flag==0):
        c1,c2,c3,c4=0,0,0,0
        print(colored('''Your Password should suffice:
1. Minimum 8 characters.
2. At least one alphabet should be of Lower Case [a-z]
3. At least one alphabet should be of Upper Case [A-Z]
4. At least 1 number or digit between [0-9].
5. At least 1 character from ['@','#','$','%','*','&','%','!' ].''','yellow'))
        pwd=input(colored("Create a password : ",'green'))
        if(len(pwd)>=8):
            for i in pwd:
                if(i.islower()):
                    c1=c1+1
                if(i.isupper()):
                    c2=c2+1
                if(i.isdigit()):
                    c3=c3+1
                if(i=='@' or i=='#' or i=='$' or i=='%' or i=='*' or i=='&' or i=='%' or i=='!'):
                    c4=c4+1
        if(c1>=1 and c2>=1 and c3>=1 and c4>=1):
            pwd2=input(colored("Re-Enter password : ",'green'))
            if(pwd==pwd2):
                password=pwd
                print(colored("Password created.",'green'))
                return password
            else:
                print(colored("Password did not match. Enter Again.",'red'))
                continue
        else:
            print(colored("Invalid Password.",'red'))
            flag=0
    

def input_password():
    flag=0
    while(flag==0):
        sugg=suggest_password()
        print(colored("Create a password.",'green'))
        print("Suggested Password : ",sugg)
        print("1. Press 1 to use suggested password.")
        print("2. Press 2 to create your own password.")
        pwd_ch=int(input(colored("Enter here : ",'green')))
        password=""
        if(pwd_ch==1):
            password=sugg
            print(colored("Password Created.",'green'))
            flag=1
        elif(pwd_ch==2):
            password=check_password()
            flag=1
        else:
            print(colored("INVALID Input.",'red'))
            flag=0
    return password
