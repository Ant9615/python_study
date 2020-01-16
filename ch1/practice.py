#1
x=['1','2','3','4','5','6']
y=['a','b','c','d','e','f']
z=['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ']
merge = x+y+z

print("#1:{!s}".format(merge))
#{0:d}에서 중괄호는 print문에 전달괴는 변수에 대한 플레이스 홀더임
#0은 넣을 변수 중 가장 첫 번째 d는 소수점 값이 없는 십진수로서 표시 즉 {0:d}는 리스트 인덱스 값의 맨 첫 번째부터 끝까지
#{1!s}에서 !s는 print문에 전달괸 값이 숫자 형식이라도 문자열로 처리
for value in range(len(merge)):
    print("{0:d}: {1!s}".format(value, merge[value]))

#2 
a=['1','2','3']
b=['a',['python','RUST','GO'],'c'] #서로 고유한 문자열 생성
w={ } #빈 dict
for index in range(len(a)):
    if a[index] not in w: #if문을 활용하여 w에 a인덱스가 없을 시에 
        w[a[index]]=b[index] #w에 a인덱스를 포함시키고 b인덱스와 매칭
for key, value in w.items():
    print("{0!s}:{1}".format(key, value))  #for문에 w의 key와 value값을 산출


#3
#리스트로 된 리스트 반복처리 
c=[['1','2','3'],['a','b','c'],['ㄱ','ㄴ','ㄷ']]

for value in c:
    max=len(value)
    output=''
    for index in range(len(value)):
        if index < (max-1):
            output +=str(value[index])+','  
        else: 
            output +=str(value[index])+'\n'     
print(output)