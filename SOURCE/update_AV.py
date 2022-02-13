# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 03:17:23 2022

@author: kimse
"""

import requests
import socket
import sqlite3
import subprocess
import os


update_SERVER = "https://raw.github.com/kimseongwoo61/test/master/version_info"
git_link = "https://github.com/kimseongwoo61/test.git"
update_version = ''

def conduct_UPDATE():
    if(check_Internet_connection() and check_Update_server()):
        if(compare_VERSION()):
            os.chdir(os.path.abspath( __file__ )+"\\..\\..\\update")
            result = subprocess.call("git clone " + git_link , shell=True)
            print(os.getcwd())
            print(result)
            if(not result):
                print(os.getcwd())
                os.chdir(os.getcwd() + "\\test")
                print(os.getcwd())
                subprocess.call("dir",shell=True)
            
       
        
# antivirus 버전을 비교한다.
def compare_VERSION(): #이상하게 DB를 열 수 없다는 에러가 발생한다. 확인 바람.
    os.chdir("C:/Users/kimse/Desktop/DP/DB/")
    con = sqlite3.connect("av_infomation.db")
    cursor = con.cursor()
    current_version = str(cursor.execute("SELECT AV_version FROM sysinfo").fetchall())[3:-4]
    

    left = list(map(int,current_version.split('.')))
    right = list(map(int,update_version.split('.')))

    
    for i in range(3):
        if(left[i] > right[i]):
            print("서버보다 버전이 높습니다!")
            return False
        elif(left[i] < right[i]):
            print("업데이트 정보를 확인하였습니다! --> version_info : "+update_version)
            return True
        elif(left[i] == right[i]):
            continue
    print("현재 최신버전 입니다!")
    print("현재버전 : %s  서버버전 : %s" % current_version, update_version)
    return False
            

# 깃허브 업데이트 서버 연결 정보를 확인한다.
def check_Update_server(): 
    res = requests.get(update_SERVER)
    if res.status_code != 200:
        print("잠시후 다시 연결 바랍니다.")
        return False
    
    else:
        global update_version
        update_version = res.text
        return True


#인터넷 연결유무를 확인한다.
def check_Internet_connection(): 
    ip_addr = socket.gethostbyname(socket.gethostname())
    if ip_addr == "127.0.0.1":
        print("인터넷 연결을 확인해 주세요!!!")
        return False
    
    else:
        return True
    
conduct_UPDATE()
