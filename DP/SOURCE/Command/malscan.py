# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:18:07 2022

@author: kimse

구현할 기능들
1. yara 룰을 관리 부분(추가, 삭제)
2. yara 룰을 기반으로 검사를 진행하는 함수(패킹 -> 악성 시그니처)
3. 코드 유사도를 검사할 수 있는 함수를 작성
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
    
def Malware_check():
    print("검사 범위를 입력해 주세요.")
def check_Packing():
def check_Signature():

def check_code_Similarity():
    print("테스트 입니다.")
    
    