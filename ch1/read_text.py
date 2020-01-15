from math import exp, log, sqrt
# 명령프롬프트나 터미널 창의 명령 줄에서 파이썬 스크립트 뒤에
# 읽을 파일을 적어서 실행하기 위해 re 모튤을 부름
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
# sys모듈을 import하면 리스트 형식의 argv 변수 사용가능
import sys
import glob
import os

# print("#1: ")
# argv는 인덱스를 가지며 argv[0]은 스크립트 이름이고
# argv[1]은 명령 줄을 통해 전달된 첫번 째 인수
# open(./text.txt, 'rt', encoding='UTF8')
input_file = sys.argv[1]
# filereader는 객체에 있는 행을 한 번에 하나씩 읽는다
# 'r'은 읽기모드로 열기
# encoding='UTF-8'을 추가하여 UTF-8로 저장된 텍스트 파일을 전부 ANSI로 다시 저장
file_reader = open(input_file, 'r', encoding='UTF-8')
# for의 body에서 각행 출력
# strip 각 행의 끝에 있는 공백, 탭, 개행문자 등을 제거
for row in file_reader:
    print(row.strip())
file_reader.close() #모든 행을 읽었을 때 filereader객체를 닫음
# 명령프롬모트나 터미널에 읽기코드가 있는 파일위치에 경로를 정하고
# " python '코드파일 명' '텍스트파일 명' "
# 텍스트 파일이 다른 경로에 잇을 때
# " python '코드파일 명' "텍스트파일 위치경로" "

# 새로운 파일 읽기 문법
# with문을 이용하여 간결하게 만든다
# with문을 사용함으로서 close가 없어지고 with문이 끝나면 파일이 자동적으로 꺼짐
print("#2: ")
with open(input_file, 'r', newline='', encoding='UTF8') as file_reader:
    for row in file_reader:
        print("{}".format(row.strip()))

# glob 이용하여 다수의 text file읽기
# 유사작업을 여러파일에 적용할 때(데이터 셋 선택, 전체 또는 부분집합의 기초통계량을 구할 떄) 유용
# 이건 왜 안되는지 생각해보자
print("#3: ")
inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*,txt')):
    with open(input_file, 'r',  encoding='UTF-8') as file_reader:
        for row in file_reader:
            print("{}".format(row.strip()))
