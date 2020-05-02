# -*- coding: utf-8 -*-
#This is Encoding-Decoding Algorithm
#Created By : Suvadip Sarkar
#Date : 02-May-2020
#I am making this as a module

from math import pow
import base64

def proc_enco(msg, key): #This is the main usable to Encode message
    key = key_word(key)
    msg = exspace(msg)
    msg = encode(msg, key)
    msg = reverse(msg)
    return(msg)

def proc_deco(msg, key): #This is the main usable to Decode message
    key = key_word(key)
    msg = reverse(msg)
    msg = decode(msg, key)
    msg = inspace(msg)
    return(msg)

def reverse(m1):
    return(m1[::-1])

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
    for i in range(keyc):
        a = []
        i = 0
        for x in str:
            cryp = ord(x) + keyc*pow(-1,i)
            a.append(chr(int(cryp)))
            i+=1
            
        a = listToString(a)
        
    message_bytes = a.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    #str = base64_message #If loop include the base64 conversion, A small message get large.
    return(base64_message)

def decode(str, keyc):
    message_bytes = str.encode('ascii')
    base64_bytes = base64.b64decode(message_bytes)
    str1 = base64_bytes.decode('ascii')
    for i in range(keyc):
        a = []
        i = 0
        for x in str1:
            if(x == " "):
                a.append(" ")
                i+=1
                continue
            cryp = ord(x) - keyc*pow(-1,i)
            a.append(chr(int(cryp)))
            i+=1
            
        a = listToString(a)
        #str = a #If loop include the base64 conversion, A small message get large. Viceversa with output.
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



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

