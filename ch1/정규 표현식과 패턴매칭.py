# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:21:09 2019

@author: STUDENT
"""
#정규 표현식과 패턴 매칭
from math import exp, log, sqrt 
import re 

# use to module 're'
# string pattern 횟수 count
#: module 're'는 다양한 메타 문자와 임의의 복잡한 패턴에 대해 생성 & 검색
str1= "닳아가는 나의 신발창 여기저기 구멍이 난 등에 멘 가방 입은 티셔츠는 너덜너덜"
str1_list=str1.split()
#~ re.compile은 텍스트 기반의 pattern을 정규 표현식으로 compile해줌
pattern=re.compile(r"나의", re.I)
#~count 초기화(pattern횟수 나타내기 위함)
count=0
for word in str1_list:
    if pattern.search(word):
        count+=1
print("1: {0:d}".format(count))

#: re.I는 pattern변수에 대/소문자 구별을 없애줌 
str2= "Please don't see just a boy caught up in dreams and fantasies"
str2_list=str2.split()
pattern=re.compile(r"please", re.I)
count=0 #~다시 count 초기화를 한 이유는 위 찾은 값과 합쳐지기에 초기화 함 
for word in str2_list:
    if pattern.search(word):
        count+=1
print("2: {0:d}".format(count))

# output to string pattern
str3="Please see me reaching out for someone I can't see" 
str3_list=str3.split()
pattern=re.compile(r"(?P<wword>someone)", re.I) #wword는 mathing word group명임 읨의 설정 가능
print("3: ")
for word in str3_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('wword')))
        
#string 일부분 대체 
str4="God, tell us the reason youth is wasted on the young"
str4_find = r"god"
pattern= re.compile(str4_find, re.I)
print("4: {:s}".format(pattern.sub("Buddha",str4))) #.sub를 이용해서 교체