# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:38:19 2022

@author: kimse
"""

import sqlite3 , os
import pandas as pd



# 로그 추출 항목을 선정한다.
#1. 활동 이력
#2. 블랙 리스트 정보
#3. 화이트 리스트 정보
#4. 시스템 정보
#5. 검역소 정보

def Extraction():
    print("1.모두추출  2.활동이력  3.블랙리스트  4.화이트리스트  5.시스템 정보  6.검역소")
    option = input("->")
    
        
    
def AV_log():
    os.chdir("C:/Users/kimse/Desktop/DP/DB/")
    con = sqlite3.connect("av_infomation.db")
    cursor = con.cursor()
    time = cursor.execute("SELECT time FROM AV_log").fetchall()
    action = cursor.execute("SELECT action FROM AV_log").fetchall()
    directory = cursor.execute("SELECT directory FROM AV_log").fetchall()
    condition = cursor.execute("SELECT condition FROM AV_log").fetchall()
    
    extraction = pd.DataFrame({
        'time' : time,
        'action' : action,
        'directory' : directory,
        
        
        })
    
    