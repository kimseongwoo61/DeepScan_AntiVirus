# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:13:59 2022

@author: kimse
"""

import os

def explan():
    print("Input format : command -[option] argument")
    print("1. scan")
    print("2. update")
    print("3. log")
    print("4. exit")
    
    print("If you want more imformation, Enter the command.")
    print("and enter q to stop the help command view.")
    
    while(True):
        command = input("help>> ")
        
        if(command == "scan"):
            scan_info()
        
        elif(command == "update"):
            update_info()
            
        elif(command == "log"):
            log_info()
            
        elif(command == "exit"):
            exit_info()
            
        elif(command == "q"):
            print("Back to the AV_shell")
            break
        
        command = input("help>> ")
        if(command == ''):
            os.system('clear')
    
def scan_info():
    print("scan")
    print("- 기능")
    print("  yara 룰 기반의 악성 시그니처 대조나 파일간의 유사도를 검사합니다.")
    print("- 옵션")
    print("  r : 하위 폴더 모두 검사하는 옵션입니다.")
    print("  s : 단일 경로만 검사지정하는 옵션입니다.")
    print("  y : yara로 정의된 룰을 기반으로 Signature 검사를 진행합니다.")
    print("  S : 입력된 파일경로들의 코드 유사도를 분석해줍니다.")
    
def update_info():
    print("update")
    print("- 기능")
    print("  프로그램의 업데이트를 진행합니다.")
    print("- 옵션")
    print("  a : 프로그램의 버전과 룰 모두 업데이트 진행합니다.")
    print("  r : rule만 업데이트를 진행합니다.")
    print("  v : 프로그램 버전만 업데이트 합니다.")

def log_info():
    print("log")
    print("- 기능")
    print("  프로그램 동작 기록을 추출하는 명령어 입니다.")
    print("- 옵션")
    print("  d : antivirus log를 저장할 경로를 지정합니다.")
    
def exit_info():
    print("exit")
    print("- 기능")
    print("  프로그램 동작 기록을 추출하는 명령어 입니다.")
    print("- 옵션")
    print("  없음.")
    
