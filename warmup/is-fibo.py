# topic:   hackerrank.com
# problem: is Fibo
# author:  frank havemann
# date:    2014-12-05

import sys

fib2 = []
fib2.append(0)
fib2.append(1)
for n in range(2,51):
    fib2.append(fib2[n-2] + fib2[n-1])
        
T = int(raw_input())

for i in range(0,int(T)):
    N = int(raw_input())
    try:
        fib2.index(N)
        print "IsFibo"
    except ValueError:
        print "IsNotFibo"