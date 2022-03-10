# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:09:13 2022

@author: kimse
"""

import yara
import os
    
def manageRule():
    print("옵션을 입력해 주세요.")
    print("1 - Delete rule")
    print("2 - Add rule")
    print("3 - exit")
    
    while(True):
        option = input(">>")
        
        if(option == "1"):
            delete_Rule()
            
        elif(option == "2"):
            add_Rule()
            
        elif(option == "3"):
            break
        
        else:
            print("옵션을 다시 입력해 주세요...")
            
    
def delete_Rule():
    
def add_Rule():