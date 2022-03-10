# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:18:07 2022

@author: kimse

구현할 기능들
1. yara 룰을 관리 부분(추가, 삭제)
2. yara 룰을 기반으로 검사를 진행하는 함수(패킹 -> 악성 시그니처)
3. 코드 유사도를 검사할 수 있는 함수를 작성
"""

    
def Malware_check(option):
    checker = deepCopy(option)
    check_dir = []
    
    print("검사 범위를 입력해 주세요.")
    file_dir = input("Malware_check>> ")
    
    if('r' in checker):
        check_dir.append(search_Dir(file_dir))
    
    if('s' in checker):
        checker_dir.append(file_dir)
    
    if('y' in checker):
        
    
    
    
def search_Dir():
    
def check_Packing():
def check_Signature():

def check_code_Similarity():
    print("테스트 입니다.")
    
def deepCopy():