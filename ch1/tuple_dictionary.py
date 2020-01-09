#tuple 
#tuple은 list와 다르게 변경이 불가능하다

#tuple 생성
i_tuple = ('x','y','z') 
print("#1: {}".format(i_tuple)) #tuple 출력 
print("#1.1:{}".format(len(i_tuple))) #tuple rotn 출력 
print("#1.2: {}".format(i_tuple[1])) #tuple의 두번째 요소 출력 
d_tuple = i_tuple + i_tuple #tuple 합연산
print("#1.3: {}".format(d_tuple)) #합연산한 새 tuple 출력 

#tuple 풀기 
하나,둘,셋 = i_tuple 
print("#2: {0} {1} {2}".format(하나,둘,셋))
v1='손흥민'
v2='메시'
print("#2.1: {} {}".format(v1, v2))
v1,v2 = v2,v1 #변수교환
print("#2.2: {} {}".format(v1,v2))  

#change tuple to list 
m_list = [1,2,3]
print("#3: {}".format(tuple(m_list)))
print("#3.1: {}".format(list(i_tuple)))


#dictionary 
#dictionary는 본질적으로 고유 식별자와 쌍을 이루는 정보로 구성된 리스트를 의미함 
#예로 business anlysis에서의 고객사전, 생산품사전, 자산사전, 매출액사전 등 
e_dict = { }
a_dict = {'하나':1,'둘':2,'셋':3}
print("#4: {}".format(a_dict))
print("#4.1: {!s}".format(len(a_dict))) #요소개수 구하기, !s는 문자열 연산할 때 이용
o_dict = {'x':'printer', 'y':5, 'z':['별','동글',9]}
print("#4.2: {}".format(o_dict))
print("#4.3: {!s}".format(len(o_dict))) #요소개수 구하기

#dictionary 내 값 접근하기
print("#5: {}".format(a_dict['둘'])) 
print("#5.1: {!s}".format(o_dict['z']))

#dictionary 복사
co_dict = a_dict.copy()
print("#6: {}".format(co_dict))

#key, values,items
#dictionary의 키, 값, 키-값 쌍에 접근하기
print("#7: {}".format(a_dict.keys())) #키 출력
print("#7.1: {}".format(a_dict.values())) #키의 값 출력 
print("#7.2:{}".format(a_dict.items())) #키와 키값 출력

#use to in, not in, get
if 'y' in o_dict:
    print("#8: {}".format(o_dict.keys()))
if 'c' not in o_dict:
    print("#8.1: {}".format(o_dict.keys()))
print("#8.2: {!s}".format(a_dict.get('셋')))
print("#8.3: {!s}".format(a_dict.get('넷')))
print("#8.4: {!s}".format(a_dict.get('넷', 'dict에 없음')))

#use to sorted()
#dictionary는 키나 값에 따라 정렬 가능하며 값이 수치라면 오름 또는 내림차순으로 정렬 가능함
#정렬결과는 item함수의 결과인 tuple들의 list가 됨
#key는 정렬기준, lambda는 runtime에서 표현식을 반환하는 짧은 함수며 item을 단일 인수로 받고, 이는 items함수가 반환할 각 키-값 tuple을 가르킴
#즉, dictionary 내 key를 기준으로 오름차순으로 dictionary의 key-value쌍을 정렬함
ordered_1=sorted(co_dict.items(), key=lambda item: item[0]) #사본 dict를 이용함으로서 원본 보존 
print("#9: (order by keys): {}".format(ordered_1)) #첫번째 키를 기준으로 정렬
ordered_2=sorted(co_dict.items(), key=lambda item: item[1]) #dict 내 값을 기준으로 오름차순으로 dict의 key-value쌍 정렬
print("#9.1: (order by keys): {}".format(ordered_2))
ordered_3=sorted(co_dict.items(), key=lambda x:x[1], reverse=True) #reverse=True는 내림차순정렬 의미
print("#9.2: (order by keys): {}".format(ordered_3))  
ordered_4=sorted(co_dict.items(), key=lambda x:x[1], reverse=False)
print("#9.3: (order by keys): {}".format(ordered_4))