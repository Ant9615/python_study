# csv파일은 숫자나 문자열로 구성되어 있는 표(or spreadsheet)형태의 데이터가 text로 저장됨
# 일반 text로 저장되므로 이를 저장하거나 전송하고 처리할 수 있는 프로그램이 다양함 
# 간단한 text edditor로도 csv파일을 처리 가능함 
 
import sys
# python에 기본으로 내장되어 있는 sys 모듈은 명령 줄에서 추가적으로 입력된 인수를 스크립트로 넘겨줌

input_file = sys.argv[1]
output_file = sys.argv[2]
# sys모듈의 argv인수는 명령 줄 실행 시에 추가적으로 입력되는 인수를 리스트 자료형으로 받고 윈도 환경에서 입력되는 csv파일을 읽고,\
# 터미널의 명령을 통해 출력 csv파일을 쓰는 데 사용되는 일반적인 형태의 명령 줄 인수임

with open(input_file, 'r', newline='') as reader:
    # input_file을 reader라는 파일 객체로 열어주는 with문 'r'은 읽기 모드
    with open(output_file, 'w', newline='') as writer:
        # output_file은 writer라는 파일 객체인 writer로 여는 명령문 'w'는 쓰기모드
        header = reader.readline()
        # reader 객체의 readline()함수를 사용하여 입력 파일의 첫 번째 행을 문자열로 읽고 이를 header라는 변수에 할당
        header = header.strip()
        # strip()함수를 사용하여 header에 있는 문자열의 양끝에서 공백, 탭 및 개행문자 등을 제거한 뒤, header에 다시 할당
        h_list = header.split(',')
        # split()를 이용하여 문자열을 쉼표 기준으로 구분하여 리스트에 할당, 리스트의 각 원소는 입력 파일의 각 열의 헤더이고, \
        # header라는 변수로 할당
        print(h_list)  # header의 값을 화면에 출력하는 print문
        writer.write(','.join(map(str, h_list))+'\n')
        # writer의 객체의 writer()함수를 사용하여 header의 각 값을 출력파일에 씀
        for row in reader:  # 반복문 for를 이용하여 입력파일의 나머지를 반복함
            row = row.strip()  # strip()을 이용하여 row라는 변수의 문자열 양끝에서 공백, 탭 및 개행문자를 제거한 뒤 row에 다시 할당
            # split()를 사용하여 문자열을 쉼표 기준으로 분리하여 리스트에 할당 list값은 각 행의 열값, row_list라는 변수에 리스트가 할당
            row_list = row.split(',')
            print(row_list)
            writer.write(','.join(map(str, row_list))+'\n')  # 값을 출력파일에 저장

            # python read_csv.py (csv파일 명) (출력하고 싶은 csv파일명)
#예제 파일 13행 cost를 $1,006,015.00으로 바꾸면 출력값이 $1 나온다. 이는 파싱이 잘 못된 경우인데 h_list = header.split(',')가\
# ,기준으로 데이터를 읽게 구성되었기에 1의 값만 나온다 이를 개선하기 위해서 스크립트의 코드를 정규표현식을 이용하여 쉼표가 포함된 문자 열 패턴을\
# 검색한 다음 행을 쉼표를 제거를 할 수 있다. 하지만, 스크립트를 복잡하게 만드는 대신 파이썬에 내장된 csv모듈을 사용할 수 있다\
# 이 묘듈은 임의적이고 복잡한 csv파일을 처리할 수 있도록 디자인 되어 있다. (read_csv2.py로)  