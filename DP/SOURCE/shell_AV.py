# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:40:52 2022

@author: kimse
옵션에 대한 인자는 해당 명령어에서 따로 입력 받도록 항.
"""
from Command import help_command, malscan, update_AV, log_manage, Rule
    
def command_SHELL():
    while(True):
        input_text = input("DP_av>> ")
        command = Ex_command(input_text)
        option = Ex_option(input_text)

        
        if(command == "scan"):
            malscan.Malware_check(option)
            
        
        elif(command == "update"):
            update_AV.conduct_UPDATE(option)
            
        elif(command == "rule"):
            Rule.management(option)
        
        elif(command == "log"):
            log_manage.Extraction(option)
            
            
        elif(command == "help"):
            help_command.explan()
        
        
        elif(command == "exit"):
            print("good afternoon, good evening, and good night!")
            break
            
        
        else:
            print("hmm... enter the command again.")
        
        
        command = ""
        option = []
   
            
   
            
def Ex_command(input_text):
    ini_word = 0
    last_word = 0 
    command = ''
    
    for i in range(0, len(input_text)):
        if(input_text[i] != ' '):
            ini_word = i
            last_word = input_text.find(' ',i)
            break
    if(last_word == -1):
        last_word = len(input_text)
        
    command = input_text[ini_word:last_word]
    return command
    


def Ex_option(input_text):
    option = []
    ini_word = input_text.find('-')
    if(ini_word == -1):
        return option
    
    last_word = input_text.find(' ',ini_word)
    
    if last_word == -1:
        last_word = len(input_text) - ini_word
        
    for i in range(ini_word+1,last_word):
        option.append(input_text[i])
        
    return option
 

   
"""def Ex_argu(input_text): #옵션 입력후 한칸 띄우고 인자를 입력해야 함!!!
    argument = []
    ini_word = input_text.find('-')
    if(ini_word == -1):
        return argument
    
    ini_word = input_text.find(' ',ini_word)+1
    last_word = input_text.find(' ',ini_word)
    
    while(True):
        if(last_word == -1):
            last_word = len(input_text)
        if(ini_word == -1):
            break
        argument.append(input_text[ini_word:last_word])
        ini_word = last_word + 1
        last_word = input_text.find(' ',ini_word)
        
    
    return argument"""