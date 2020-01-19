# 특정 행만 출력하고 싶을 때 즉,
# 1. 특정 조건을 충족하는 행을 필터링
# 2. 특정 집합의 값을 포함하는 행을 필터링
# 3. 정규 표현식을 활용해 필터링 등

# 1. 특정 조건을 충족하는 행을 필터링
# 두 가지 조건에 부합하는 행의 값을 판별하고 그 조건을 충족하는 행으로 구성된 하위 데이터셋을 출력 파일로 작성
import csv
import sys 

in_file=sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r', newline='') as inf:
    with open(out_file, 'w', newline='') as outf:
        freader = csv.reader(inf)
        fwriter = csv.writer(outf) #여기까지 읽기랑 같음
        header = next(freader)
        fwriter.writerow(header)
        for row_list in freader:
            supplier=str(row_list[0]).strip()
            cost=str(row_list[3].strip('$').replace(',',''))
            if supplier == 'Supplier Z' or float(cost) >600.0:
                fwriter.writerow(row_list)
                print(row_list)