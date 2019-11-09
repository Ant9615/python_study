# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:32:39 2019

@author: STUDENT
"""

print("1: {0:s}".format('i\'m enjoy learning python'))
print("2: {0:s}".format("연구팀은 이 논문에서\
      압전섬유의 토포그래피를 조절하는\
      나노 패터닝 기술을 이용하여 다양한 형태의 3D 나노지지체를 개발하고\
      이를 신경조직 재생 분야에 \
      적용했다"))
print("3: {0:s}".format('''이 연구는 향후 재생이 어려운 신경세포 재생 분야에 활용될 수 있을 것으로 예상된다.'''))
print("4: {0:s}".format("""이 연구는 향후 재생이 어려운 신경세포 재생 분야에 활용될 수 있을 것으로 예상된다."""))

str1= "그래그래"
str2= "하모니카 솔로~" 
sen=str1+str2
print("5: {0:s}".format(sen))
print("6: {0:s} {1:s}{2:s}{3:s} {4:s}{5:s}".format("그래"*2, "하모니ㅋ", "ㅏ"*3, "~"*3, "솔로", "!"*5 ))
#문자길이 출력
m=len(sen)
print("7: {0:d}".format(m))

#split
str3="그대여 우리 같이 걸어요"
str3_list1 = str3.split()
str3_list2 = str3.split(" ", 3)
print("8: {0}".format(str3_list1))
print("9: 첫번 째: {0} 두번 째: {1} 세번 째: {2} "\
      .format(str3_list2[0], str3_list2[1], str3_list2[2]))
str4 = "사랑하는, 그대와, 단둘이, 손잡고, 알, 수, 없는, 이, 거리를, 둘이, 걸어요"
str4_list = str4.split(',')
print("10: {0}".format(str4_list))
print("11: {0} {1} {2} {3}".format(str4_list[1], str4_list[3],\
      str4_list[-3], str4_list[-1]))

print("ow: {0}".format(str3_list2))

