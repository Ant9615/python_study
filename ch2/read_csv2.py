#기본 파이썬 모듈 사용하기 
import sys
import csv 

input_file=sys.argv[1]
output_file=sys.argv[2]

with open(input_file, 'r', newline='') as infile:
    with open(output_file, 'w', newline='') as outfile:
        freader = csv.reader(infile, delimiter=',')
        fwriter = csv.writer(outfile, delimiter=',')
        for row_list in freader:
            fwriter.writerow(row_list)
            print(row_list)