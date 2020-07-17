# -*- coding: utf-8 -*-
#This is UI module
#Created By : Suvadip Sarkar
#Date : 02-May-2020

from crypto import proc_enco,proc_deco
import pyperclip

def rep(selec):
    if(selec > 3):
        print("\nInvalid selection {}, Select 1 or 2. Please Try Again".format(selec))
        selec = int(input("\nEnter 1 to Encode\nEnter 2 to Decode\nEnter 3 to Exit : "))
        return(rep(selec))
    else:
        return selec
    
def convert():            
    try:
        print("\n\n\n******Welcome to Encryption Operation******")
        select = rep(int(input("\nEnter 1 to Encode\nEnter 2 to Decode\nEnter 3 to Exit : ")))
        if(select == 3):
            exit()
            
        msg = str(input("\nEnter your messege : "))
        key = str(input("\nEnter Today's key : "))
        
         
        if(select == 1):
            msg = proc_enco(msg, key)
            print("\nEncoded = ",msg,"\n\nMessage is automatically copied to clipboard")
        elif(select == 2):
            msg = proc_deco(msg, key)
            print("\nDecoded = ",msg,"\n\nMessage is automatically copied to clipboard")
                
        pyperclip.copy(msg)
            
    except ValueError:
        print("\nPlease input only integer. Please try again")
        convert()
