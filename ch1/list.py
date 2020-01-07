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
print("#2.2: 5 is in b_list {} time".format(b_list.count(5)))  # count는 리스트 내에서 특별한 값을 보여줌
