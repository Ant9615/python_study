#자료형과 자료구조에 대해 암묵적으로 가정하고 프로그램을 작성할 수 있지만
#이 가정을 따르지 않는 데이터의 경우 프로그램 오류를 발생시킬 수 있다.
#try-except

def GetMean(numericValues):
    return sum(numericValues)/len(numericValues)

m_list = []

#short 
try:    #실행할 code를 try안에 배치 
    print("#1: {}".format(GetMean)) 
except ZeroDivisionError as detail:  #다른 잠재적 error들을 처리하고 도움이 되는 error massage 출력 
    print("#1.1: (error): {}".format(float('nan')))
    print("#1.2: (error): {}".format(detail))

#long(try-except-else-finally)
try: 
    result = GetMean(m_list)
except ZeroDivisionError as detail: #list에 element가 없으므로  
    print("#2: (error): {}".format('none'))
    print("#2.1: (error): {}".format(detail))
else: #try에 문제가 없을 경우 실행
    print("#2.2: (the mean is): {}".format(result))
finally: 
    print("#2.3: (finally): Finally block is executed every time")