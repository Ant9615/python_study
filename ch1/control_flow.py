#if-else 
x=5 
if x>=5 or x!=9:
    print("#1: {}".format(x))
else: 
    print("#1: 조건문에 안맞음") 

#elif 
if x>7: 
    print("#2: x는 7보다 큼")
elif x>1 and x<=3:
    print("#2: x는 1보다 크고 3보다 작음")
else: 
    print("#2: 사실 X는 5임")

#for 
y=['heart shaker', 'likey', 'signal','knock knock','tt','cheer up']
z=['병장','상병','일병','이병','훈련병']

for twice in y:
    print("#3: {!s}".format(twice))

#{0!s}을 선언하여 z의 요소 수만큼, {1!s}를 선언하여 요소를 순서대로 출력
for rank in range(len(z)):
    print("#3.{0!s}: {1!s}".format(rank, z[rank]))

#하나의 시퀀스에서 생성된 인덱스들을 이용하여 다른 시퀀스의 동일한 인덱스에
#해당하는 값에 접근하는 방법을 보여줌
for q in range(len(y)):
    if y[q].startswith('Q'):
        print("#3.5: {!s}".format(y[q])) 

#dictionary의 key와 value에 반복해서 접근
o_dict = {'x':'printer', 'y':5, 'z':['별','동글',9]}
for key, value in o_dict.items(): #dict내의 각 key-value tuple을 출력
    print("#3.6: {!s}".format(key,value))


#list comprehension
#리스트축약을 이용해서 특정 해를 구하기 
l_data=[[1,2,3],[4,5,6],[7,8,9]]
row_keep = [row for row in l_data if row[2]>5] #행의 두 번째 인덱스에 위치한 값이 5보다 큰 인덱스만 남겨! 
print("#4: {}".format(row_keep))

#set comprehension
#tuple의 집합을 추출하는 방법 
t_data=[(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_tules1 = {x for x in t_data}
print("#4.1: {}".format(set_tules1))
set_tules2 = set(t_data)
print("#4.2: {}".format(set_tules2)) # #2와 같음 

#dictionary comprehension
#dict 축약을 이용하여 특정 조건에 부함하는 dict의 key-vlaue 쌍들의 부분집합 선택
d_data={'c1':78, 'c2':92, 'c3':128}
d_data_results={key: value for key, value in d_data.items() if value>80}
print("#4.3: {}".format(d_data_results))

#while
#body가 실행되어야 할 횟수를 이미 알고 있을 경우 유용함, 알지 못할 때는 for문 이용 
k=1 
while k<=6:
    print("#5: {!s}".format(k))
    k+=1

    