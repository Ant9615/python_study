# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:23:05 2019

@author: user
"""

from math import exp, log, sqrt 
import re 
from datetime import date, time, datetime, timedelta 

#date 객체와 datetime 객체
today=date.today()
print("1: today is {0!s}".format(today))
print("2: this year is {0!s}".format(today.year))
print("3: this month is {0!s}".format(today.month))
print("4: today is {0!s}".format(today.day))
current_datetime=datetime.today()
print("5: current {0!s}".format(current_datetime))

#timedelta 함수를 이용하여 새로운 날짜 계산하기 
#~timedelta는 날짜, 초, 마이크로초 등 시간 단위를 저장하고, 고유한 값으로 정규화 함 
one_day=timedelta(days=-1)
yesterday=today+one_day 
print("6: yesterday is {0!s}".format(yesterday))
#~timedelta는 60, 3600초(1시간 초 단위로 하면 3600), 7일 단위로 계산
#~그래서 -8하면 일자는 -1일, 시간은 일일 초로 한산한 \86400초 - 288000(시간당 3600초*8시간)=57600초
eight_hours=timedelta(hours=-8)
print("7: {0!s}, {1!s}"\
      .format(eight_hours.days, eight_hours.seconds))

#두 날짜 사이 날짜 차이 계산 
date_diff=today-yesterday
print("8: difference between today and yesterday is {0!s}"\
      .format(date_diff))
#~str은 결과를 하나의 문자열로 변환한다, [0]은 앞에 만들어진 리스트의 첫 번째 원소를 선택함  
print("9: difference between today and yesterday is {0!s} day".format(str(date_diff).split()[0]))

#strftime함수를 이용하여 date 객체를 특정 형식의 문자열로 만들기 
print("10: {:s}".format(today.strftime('%m/%d/%Y'))) #{0!s}로 해도 상관x
print("11: {:s}".format(yesterday.strftime('%b%d,%Y')))
print("12: {:s}".format(today.strftime('%Y-%m-%d')))
print("13: {0!s}".format(yesterday.strftime('%B,%d,%Y')))

#날짜문자열을 datetime 객체 생성한 후 date객체 출력과 날짜부분만 출력하기 
date1=today.strftime('%m/%d/%Y')
date2=yesterday.strftime('%b%d,%Y')
date3=today.strftime('%Y-%m-%d')
date4=yesterday.strftime('%B,%d,%Y')
#~각 다른 문자열들을 datetime 객체로 일정하게 통합
print("14: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("15: {!s}".format(datetime.strptime(date2, '%b%d,%Y')))
#~날짜만 출력 
print("16: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("17: {!s}".format(datetime.date(datetime.strptime(date4, '%B,%d,%Y'))))
