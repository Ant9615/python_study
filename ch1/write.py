# write는 개별 문자열을 파일에 작성하고 writelines 함수는 일련의 문자열을 파일에 작성
# range와 len 함수를 조합하여 리스트 내 값들의 인덱스를 추적하여 각 값 사이에 구분자를 넣고 개행문자를 넣어보자

# 스크립트에 코드 추가
import sys

# m_letters=['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ']
# max_index=len(m_letters)
output_file = sys.argv[1]
# filewriter=open(output_file,'w',encoding='UTF8') #한글이면 인코딩은 무조건 해주자
# for index_value in range(len(m_letters)):
# if-else문은 리스트의 마지막 원소와 나머지 모든 원소사이 구분 해줌 if 조건은 마지막 원소 전까지 원소 뒤에 \t탭을 추가
    # if index_value < (max_index-1):
    #     filewriter.write(m_letters[index_value]+'\t')
# else는 마지막 원소 뒤에 띄어줄 것
#     else:
#         filewriter.write(m_letters[index_value]+'\n')
# filewriter.close()
# print("작성함")

# 파일 내용 추가
m_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_ele = len(max(m_num))
filewriter = open(output_file, 'a', encoding='UTF8')
for index_value in range(len(m_num)):
    if index_value < (max_ele):
        filewriter.write(str(m_num[index_value]+','))
    else:
        filewriter.write(str(m_num[index_value]+'\n')
filewriter.close() #아 이거 왜 syntax error 뜨냐;
print("추가")
#실행은 python write.py "./파일명.txt"
#csv파일 작성은 python write.py "./파일명.csv"