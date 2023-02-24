import csv
import re
import sys
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

class Validate:
    def signup(self):
        i=0
        j=0
        while (i==0):            
            print("----Make sure your email id in the format like abcd123@gmail.com ")
            email =  input("Enter your Email_id :")
            if(re.search(regex,email)):    
                i+=1
                status=0
                print("Valid Email")
            else:   
                print("Invalid Email")  
        
        while (j==0):
            print("----Make sure your password is at lest 8 letters with a number and a capital letter in it---- ")
            password = input("Enter a password: ")
            if (re.search('[0-9]',password) != None) and (len(password) > 8) and (re.search('[A-Z]',password) != None):
                j+=1
                flag=0
                print("Valid Password")
            else:
                print("Reenter your password")
        if flag==0 and status==0:
            with open("username.csv","r") as user:
                    out = csv.reader(user)
                    for i in out:
                        if i[0]==email and i[1]==password:
                            flag=1
                            break
                    if flag==0:
                        with open("username.csv",mode="a",newline="") as new:
                            write= csv.writer(new,delimiter=",")
                            write.writerow([email,password])
                            print("\n\tSIGNED UP SUCCESSFULLY\n")
                            
                    else:
                        print("Your account already exists")
    def login(self):
        email=input("Enter your login mail id:")
        password=input("Enter your login password:")
        f=0
        with open("username.csv",mode="r") as d:
            reader=csv.reader(d,delimiter=",")
            for row in reader:
                if row[0]==email and row[1]==password:
                    print ("SUCCESSFULLY LOGGED IN")
                    f=f+1
            if(f<1):
                print("Either your email id or password is incorrect")
                print("*************************")
                print("\tRE-ENTER || CANCEL")
                print("\t  1          2")
                print("*************************\n")
                choice=int(input("Enter your choice:"))
                if choice==1:
                        s=Validate
                        s.login()
                elif choice==2:
                        sys.exit()
                else:
                        print("Invalid Choice")
                        
                    
#print(" ___________________________")
#print("|        SIGNUP/LOGIN       |")
#print("|__________1______2_________|")
#choice=int(input("\nSELECT YOUR CHOICE:"))
#if choice==1:
#       
#        signup()
#else:
#       
#        login()



