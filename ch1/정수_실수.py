# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:10:29 2019

@author: STUDENT
"""
from math import exp, log, sqrt

#output to integer num. 
x=9
print("#1.1: {0}".format(x+1))
#~square
print("#1.2: {0}".format(3**4))
#~division
print("#1.3: {0}".format(int(8.3)/int(2)))

#output to real num.
#~ .3f는 소수점 3자리까지 output
print("#2.1: {0:.3f}".format(8.3/2.5))
y=2.5
print("#2.2: {0:.3f}".format(y*4))
print("#2.3: {0:.2f}".format(y/float(7))) #float은 실수
print("#2.4: {0:.1f}".format(6.0/6))
#~use to math library
print("#2.5: {0:.3f}".format(exp(3)))
print("#2.6: {0:.2f}".format(log(2)))
print("#2.6: {0:.4f}".format(sqrt(9)))