import sys
import pandas as pd
# 판다스를 활용하면 간결하게 코드를 작성할 수 있음

input_file = sys.argv[1]
output_file = sys.argv[2]

frame = pd.read_csv(input_file)
print(frame)
frame.to_csv(output_file, index=False)
# 입력파일이 외부에 있을 때 python pd_read_csv.py (파일path) (출력할 파일명)
# 안돌아 가면 pip install pandas
