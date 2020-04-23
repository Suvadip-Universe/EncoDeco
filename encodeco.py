
from math import pow
import pyperclip

def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

def key_word(k):
    s,d = 0,0
    for x in k:
        s = s + ord(x)
    
    while((s//10) >= 1):
        while(s > 0):
            d += (s%10)
            s = s//10
        s = d
        d = 0
    return(s)

def encode(str, keyc):
    a = []
    i = 0
    for x in str:
        cryp = ord(x) + keyc*pow(-1,i)
        a.append(chr(int(cryp)))
        i+=1
        
    a = listToString(a)
    return(a)

def decode(str, keyc):
    a = []
    i = 0
    for x in str:
        if(x == " "):
            a.append(" ")
            i+=1
            continue
        cryp = ord(x) - keyc*pow(-1,i)
        a.append(chr(int(cryp)))
        i+=1
        
    a = listToString(a)
    return(a)
    
def exspace(msgs):
    lis = []
    for x in msgs:
        if(x == " "):
            lis.append("`")
            continue
        lis.append(x)
    msgs = listToString(lis)
    return(msgs)

def inspace(msgs):
    lis = []
    for x in msgs:
        if(x == "`"):
            lis.append(" ")
            continue
        lis.append(x)
    msgs = listToString(lis)
    return(msgs)

def rep(selec):
    if(selec > 3):
        print("\nInvalid selection {}, Select 1 or 2. Please Try Again".format(selec))
        selec = int(input("\nEnter 1 to Encode\nEnter 2 to Decode\nEnter 3 to Exit : "))
        return(rep(selec))
    else:
        return selec
    
def reverse(m1):
    return(m1[::-1])

def convert():            
    try:
        select = rep(int(input("\nEnter 1 to Encode\nEnter 2 to Decode\nEnter 3 to Exit : ")))
        if(select == 3):
            exit()
            
        msg = str(input("\nEnter your messege : "))
        
        key = key_word(str(input("\nEnter Today's key : ")))
        
         
        if(select == 1):
            msg = exspace(msg)
            msg = encode(msg, key)
            msg = reverse(msg)
            print("\nEncoded = ",msg,"\nMessage is automatically copied to clipboard")
        elif(select == 2):
            msg = reverse(msg)
            msg = decode(msg, key)
            msg = inspace(msg)
            print("\nDecoded = ",msg,"\nMessage is automatically copied to clipboard")
                
        pyperclip.copy(msg)
            
    except ValueError:
        print("\nPlease input only integer. Please try again")
        convert()


print("\n******Welcome to Encryption Operation******")
convert()
while(1):
    print("\n******Welcome to Encryption Operation******")
    convert()


