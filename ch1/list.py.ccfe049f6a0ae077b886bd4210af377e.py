from math import exp, log, sqrt
import re 
from datetime import date, time, datetime, timedelta
from operator import itemgetter

# 리스트생성
a_list = [1, 2, 3]
# 리스트출력
print("#1: {}".format(a_list))
# len은 list의 element 수를 표현
print("#1.1: a_list has {} elements.".format(len(a_list)))
# list안의 maximum, minimum 값 return
print("#1.2: the maximum value in a_list is {}".format(max(a_list)))
print("#1.3: the minimum value in a_list is {}".format(min(a_list)))
# 문자 list
b_list = ['prin', '5', ['star', 'circle', 9]]
print("#2: {}".format(b_list))
# element가 3개인 이유는 리스트 안에 또 다른 리스트가 있기에 하나로 묶어서 하나의 element로 인식함
print("#2.1: b_list has {} elements".format(len(b_list)))
print("#2.2: 5 is in b_list {} time".format(
    b_list.count(5)))  # count는 리스트 내에서 특별한 값을 보여줌
# index
print("#3: {}".format(a_list[0]))  # 첫번째 리스트 요소
print("#3.1: {}".format(a_list[2]))
print("#3.2: {}".format(a_list[-1]))  # 맨 마지막 요소
print("#3.3: {}".format(a_list[-2]))  # 맨 뒤에서 두번째 요소
print("#3.4: {}".format(a_list[-3]))
print("#3.5: {}".format(b_list[1]))
print("#3.6: {}".format(b_list[-1]))  # 맨 마지막 요소

# separate list
print("#4: {}".format(a_list[0:3]))  # 요소 모두 출력
print("#4.1: {}".format(a_list[0:2]))  # 리스트의 첫번째 두번째만 부분집합으로 묶어 출력
print("#4.2: {}".format(b_list[:2]))  # 리스트의 두번째 요소까지 출력
print("#4.3: {}".format(b_list[1:]))  # 리스트의 두번째부터 마지막까지 출력

# list copy & merge
n_list = a_list[:] + b_list[:]  # 기존 두 리스트를 합침
print("#5: {}".format(n_list))

# in & not in
a = 2 in a_list
print("#6: {}".format(a))
if 2 in a_list:
    print("#6.1: {}".format(a_list))
b = 6 not in b_list
print("#6.2: {}".format(b))
if 6 not in a_list:
    print("#6.3:{}".format(a_list))

#append, remove, pop
a_list.append(4)  # append는 list 마지막에 추가
for i in range(5, 9):  # 5부터 8까지 추가
    a_list.append(i)
print("#7: {}".format(a_list))
a_list.insert(2, 10) #2 뒤에 10 추가(원하는 자리에 추가)
print("#7.1: {}".format(a_list))
a_list.extend(b_list) #a_list에 b_list 추가
print("#7.2:{}".format(a_list))
a_list.remove(8) #list에 8제가
print("#7.3: {}".format(a_list))
a_list.pop()#list의 마지막 요소 제거
print("#7.3: {}".format(a_list))

#reverse 
a_list.reverse() #list 반전
print("#8: {}".format(a_list))

#sort & sorted 
u_list = [9,3,6,7,3,6,4,5,1]
co_list = u_list[:]
print("#9:{}".format(u_list)) #정렬 전
u_list.sort() #정렬
print("#9.1:{}".format(u_list)) #정렬 후
m_list=[[1,2,3,4], [4,3,1,2], [3,2,4,1]]
m_list_sorted = sorted(m_list, key=lambda index_value: index_value[3])
print("#9.2: {}".format(m_list_sorted)) #index 3에 위치한 값에 따라 정렬(4번째 값에 의해 index가 오름차순으로 정렬)
#위의 math package 등을 import 해준 후 
m_lists = [[123,2,2,555], [33,45,333,667],[45,68,23,111],[1,222,33,81],[6,33,441,67],[9999,11,244,41]]
m_lists_sorted = sorted(m_lists, key=itemgetter(3,1))
print("#9.3:{}".format(m_lists_sorted)) #3번째 index에 위치한 값에 따라 정렬하고, 이 정렬 순서를 유지하면서 1번째 index에 위치한 값에 따라 정렬 수행

