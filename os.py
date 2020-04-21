############################################################
#####################  A S NANDANUNNNI  ####################
############################################################

import random
import datetime
import time
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def off():
    print("\n\n")
    print("\t      *      ")
    print("\t     / \     ")
    print("\t*---*---*---*")
    print("\t \ /     \ / ")
    print("\t  *       *  ")
    print("\t / \     / \ ")
    print("\t*---*---*---*")
    print("\t     \ /     ")
    print("\t      *      ")
    time.sleep(0.8)
    clear()
    exit()

def addcontact():
    clear()
    print("\n\n\tA D D   C O N T A C T S")
    f=open("contacts.txt","a")
    cname=input("\n\tName : ")
    f.write(cname)
    f.write("\n")
    cphno=input("\tPhone Number : ")
    f.write(cphno)
    f.write("\n")
    f.close()
    clear()
    a=int(input("\n\t1. Add Contact\t2. Back\n\n\t    Menu : "))
    if a==1:
        addcontact()
    else:
        return None

def dispcontact():
    clear()
    print("\n\n\t\tC O N T A C T S\n")
    f=open("contacts.txt","r")
    contacts=f.readlines()
    j=0
    for i in contacts:
        if j%2==0:
            print(i,end="")
        else:
            print(i)
        j=j+1
    f.close()
    del contacts
    input("\n\t    Continue... ")

def editcontact():
    dispcontact()
    print("\n\n\tE D I T   C O N T A C T")
    a=input("\n\n\tOld Name : ")
    b=input("\n\tOld Phone Number : ")
    c=int(input("\n\t1. Edit Name\n\t2. Edit phone number\n\t    Menu : "))
    if c==1:
        d=input("\n\tNew Name : ")
    else:
        d=input("\n\tNew Phone Number : ")
    f=open("contacts.txt","r")
    cont=f.readlines()
    f.close()
    if c==1:
        cont=[i.replace(a,d) for i in cont]
    else:
        cont=[i.replace(b,d) for i in cont]
    f=open("contacts.txt","w")
    f.writelines(cont)
    f.close()
    clear()
    return None

def deletecontact():
    dispcontact()
    print("\n\n\t D E L E T E   C O N T A C T")
    a=input("\n\n\tName : ")
    b=input("\n\tPhone number : ")
    f=open("contacts.txt","r")
    cont=f.readlines()
    f.close()
    cont=[i.replace(a,"",1) for i in cont]
    cont=[i.replace(b,"",1) for i in cont] 
    f=open("contacts.txt","w")
    f.writelines(cont)
    f.close()
    return None

def calculator():
    clear()
    print("\n\n\t\tC A L C U L A T O R")
    a=float(input("\nEnter first number: "))
    b=input("\nEnter the operator: ")
    c=float(input("\nEnter second number: "))
    f=0
    if b=='+':
        d=a+c
    elif b=='-':
        d=a-c
    elif b=='*':
        d=a*c
    elif b=='/':
        if c==0:
            print("\ndivision by 0 is not possible..!")
            f=1
        else:
            d=a/c
    elif b=='^':
        d=a**c
    elif b=='%':
        d=a%c
    else:
        print("\nInvalid Operator")
        f=1
    if f==0:
        print("\n",a,b,c,"=",d)
    a=int(input("\n\n\t1. Continue \t2. Back \n\n\t Menu : "))
    if a==1:
        calculator()
    else:
        return None
############################################################
######################## HANGMAN GAME ######################

def hangman():
    def title():
        clear()
        print("\n\t-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t-=-=-=-  H A N G M A N  -=-=-=-")
        print("\t=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\n\t\tGuess the Word..!!!")

    def victory():
        print("\n\n\tThe word is",ans)
        print("\n\n\t*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        print("\t.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.")
        print("\t*.*.*.*  V I C T O R Y  *.*.*.*")
        print("\t.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.")
        print("\t*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

    def pause():
        input("\n\t   Press Enter to continue...")

    words=["apple","orange","grapes","banana","pineapple","jackfruit"]
    user=["__p__","__a__e","__a__s","__n__a","__n__p__e","__c__r__t"]
    a=random.randint(0,5)
    ans=words[a]
    guess=words[a]
    del a
    l=len(ans)
    for i in range(1,l+1):
        if i%3!=0:
            guess=guess.replace(guess[i-1],str(i),1)
    h=5
    f=0
    while h>0:
        title()
        print("\n\n\t",end="")
        for i in range(l):
            if guess[i].isdigit()==True:
                print("__",end=" ")
            else:
                print(guess[i],end=" ")
        print("\n\n\tLife : ",h)
        z=input("\n\n\tGuess a letter : ")
        f=0
        for i in range(l):
            if z==ans[i]:
                f=f+1
                guess=guess.replace(guess[i],ans[i],1)
        if f>0:
            if guess==ans:
                victory()
                z=int(input("\n\t  1. Play Again \t2. Back\n\n\tMenu : "))
                if z==1:
                    hangman()
                else:
                    return None
        else:
            h=h-1
            print("\n\n\tThe word doesn't contain",z)
            pause()
        title()
        print("\n\n\t",end="")
        for i in range(l):
            if guess[i].isdigit()==True:
                print("__",end=" ")
            else:
                print(guess[i],end=" ")
        print("\n\n\tLife : ",h)
        y=input("\n\n\tDid you get the word ? (y/n) : ")
        if y=='y':
            temp=str(input("\n\t    Your Answer : "))
            if temp==ans:
                victory()
                z=int(input("\n\t  1. Play Again \t2. Back\n\n\tMenu : "))
                if z==1:
                    hangman()
                else:
                    return None
            else:
                h=h-1
                print("\n\n Wrong..!\n",h," life remaining.")
                pause()
    if h==0:
        print("\n\n\t F A I L E D")
        z=int(input("\n\t  1. Play Again \t2. Back\n\n\tMenu : "))
        if z==1:
            hangman()
        else:
            return None

####################### HANGMAN GAME #######################
############################################################

############################################################
############################ HOME ##########################

def home():
    clear()
    print("\n\n")
    clock=datetime.datetime.now()
    print("\t\t",clock.day,"/",clock.month,"/",clock.year)
    print("\t\t   ",clock.hour,":",clock.minute)
    print("\n\n  1. CONTACTS\t2. NOTES\t3. CALCULATOR\n\n  4. GAMES\t5. REFRESH\t6. POWER OFF")
    a=int(input("\n\tMenu : "))
    b=int()
    if a==1:
        clear()
        print("\n\n\tC O N T A C T S")
        print("\n\n  1. Add Contact\t2. View Contacts\n\n  3. Edit Contact\t4. Delete Contact\n\n  5. Back")
        b=int(input("\n\tMenu : "))
        if b==1:
            addcontact()
            home()
        elif b==2:
            dispcontact()
            home()
        elif b==3:
            editcontact()
            home()
        elif b==4:
            deletecontact()
            home()
        else:
            home()
    elif a==2:
        home()
    elif a==3:
        clear()
        calculator()
        home()
    elif a==4:
        clear()
        print("\n\n  1. Hangman\t2. (Coming Soon)\t3. Back")
        b=int(input("\n\tMenu : "))
        if b==1:
            hangman()
            home()
        elif b==3:
            home()
        else:
            home()
    elif a==5:
        home()
    elif a==6:
        clear()
        off()
    else:
        home()

########################### HOME ###########################
############################################################

home()