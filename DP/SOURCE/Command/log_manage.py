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
    os.chdir("C:/Users/kimse/Desktop/DP/DB/")
    print("1.모두추출  2.활동이력  3.블랙리스트  4.화이트리스트  5.시스템 정보  6.검역소")
    option = input("->")
    
        
    
def AV_log():
    con = sqlite3.connect("av_infomation.db")
    cursor = con.cursor()
    
    time = list(cursor.execute("SELECT time FROM AV_log").fetchall()
    action = cursor.execute("SELECT action FROM AV_log").fetchall()
    directory = cursor.execute("SELECT directory FROM AV_log").fetchall()
    condition = cursor.execute("SELECT condition FROM AV_log").fetchall()
    
    cursor.close()
    
    extraction = pd.DataFrame({
        'time' : time,
        'action' : action,
        'directory' : directory,
        'condition' : condition
        })
    
    os.chdir("C:/Users/kimse/Desktop/DP/Extract_log")
    extraction.to_excel('AV_log.xlsx')
    
    
    
def Quarn():
    con = sqlite3.connect("av_infomation.db")
    cursor = con.cursor()
    
    time = list(cursor.execute("SELECT filename FROM Quarn").fetchall()
    action = cursor.execute("SELECT save_dir FROM Quarn").fetchall()
    directory = cursor.execute("SELECT SHA256 FROM Quarn").fetchall()
    condition = cursor.execute("SELECT MD5 FROM Quarn").fetchall()
    
    cursor.close()
    
    extraction = pd.DataFrame({
        'filename' : time,
        'action' : action,
        'directory' : directory,
        'condition' : condition
        })
    
    os.chdir("C:/Users/kimse/Desktop/DP/Extract_log")
    extraction.to_excel('Quarn.xlsx')
    
    
def black_list():
    con = sqlite3.connect("av_infomation.db")
    cursor = con.cursor()
    
    time = list(cursor.execute("SELECT directory FROM black_list").fetchall()
    action = cursor.execute("SELECT filename FROM black_list").fetchall()
    directory = cursor.execute("SELECT create_time FROM black_list").fetchall()
    condition = cursor.execute("SELECT SHA256 FROM black_list").fetchall()
    
    cursor.close()
    
    extraction = pd.DataFrame({
        'time' : time,
        'action' : action,
        'directory' : directory,
        'condition' : condition
        })
    
    os.chdir("C:/Users/kimse/Desktop/DP/Extract_log")
    extraction.to_excel('black_list.xlsx')
    


    
    