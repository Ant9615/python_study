# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:53:38 2019

@author: STUDENT

"""

#join
str1="알 수 없는 이 거리를 둘이 걸어요"
str1_list=str1.split(" ")
print("1: {0}".format('. '.join(str1_list)))

#strip
str2="   알 수 없는 이 거리를    둘이 걸어요\t\t  \n"

print("2: str2:{0:s}".format(str2))
str2_lstrip=str2.lstrip()
print("3: lstrip: {0:s}".format(str2_lstrip))
str2_rstrip=str2.rstrip()
print("4: rstrip: {0:s}".format(str2_rstrip))
str2_strip=str2.strip()
print("5: strip: {0:s}".format(str2_strip))

str3="$$알 수 없는 이 거리를   둘이 걸어요.__---+++"
print("6: {0:s}".format(str3))
str3_strip=str3.strip('$_-+')
print("7: {0:s}".format(str3_strip))

