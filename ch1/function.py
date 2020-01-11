import numpy as np

#user defined function
#숫자 시퀀스의 평균 계산
def GetMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) >0 \
        else float('null') #if-else를 이용하여 list내에 numeric 요소가 있는지 확인 

m_list=[2,3,4,5,67,123,4567,8764,124553,67532]
print("#1: list elements mean is {!s}".format(GetMean(m_list)))

#numpy 모듈을 이용하여 mean값 출력 
print("#2: list elements mean is {!s}".format(np.mean(m_list)))