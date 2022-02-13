# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 20:33:30 2022

@author: kimse

안녕하세요!!! 
이번에 제가 직접 AntiVirus를 제작하고 있습니다.
검사 시간이 상당하지만... 최적화 및 다양한 기능을 구축할 수 있도록 하겠습니다.
"""
from SOURCE import update_AV
from SOURCE import log_manage


title =  """ ______                         ______                      \n"""                     
title += """(______)                       / _____)                     \n"""                     
title += """ _     _  _____  _____  ____  ( (____    ____  _____  ____  \n""" 
title += """| |   | || ___ || ___ ||  _ \  \____ \  / ___)(____ ||  _ \ \n""" 
title += """| |__/ / | ____|| ____|| |_| | _____) )( (___ / ___ || | | |\n"""
title += """|_____/  |_____)|_____)|  __/ (______/  \____)\_____||_| |_|\n"""
title += """                       |_|                                  \n"""


print(title)
print("동작을 선택해 주세요.")
print("1. 검사   2. 업데이트 확인  3. 로그 추출")

operation = int(input("-> "))


if(operation == 1):
    Malware_check()

elif(operation == 2):
    update_AV.conduct_UPDATE()

elif(operation == 3):
    log_manage.Extraction()
    
