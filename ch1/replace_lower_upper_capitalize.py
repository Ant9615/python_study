# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:55:42 2019

@author: STUDENT
"""
#replace~strip와 반대
str1="저물어 가는 해는 약속을 하지 않아요 오늘이 지나가도 날 잊지 않길 바라요."
str1_replace=str1.replace(" ", "!@!")
print("1: {0:s}".format(str1_replace))
str1_replace1=str1.replace(" ", ",")
print("2: {0:s}".format(str1_replace1))

#lower/upper/capitalize
#~lower는 대문자를 소문자로
str2="보통날이' 아름다운 건 You란 기적 때문이죠 내 Day를 밝혀주는 건 그대란 NAME의 빛이죠"
print("3: {0:s}".format(str2.lower()))
#~upper는 lower와 반대
str3="왠지' sleep은 안 오고 사는 걱정에 뒤척이다 괜시리 hANDFONE만 만지작대다 뭐가 그렇게 바쁘다고"
print("4: {0:s}".format(str3.upper()))
#~capitalize는 맨첫번째 문자만 대문자, 나머지는 소문자 
str4="휴가 once도 못 떠나고 이 SUMMER 그냥 이렇게 보내도 될까"
print("5: {0:s}".format(str4.capitalize()))
#~~문자 분리하고 반복문을 이용하여 capitalize
str4_list=str4.split()
for word in str4_list:
    print("6: {0:s}".format(word.capitalize()))
    
    