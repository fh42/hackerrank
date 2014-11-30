# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

cntTestCases = int(raw_input())

for i in range(0,int(cntTestCases)):
    count = 0
    number = raw_input()

    for digit in number:
        if digit == '0':
            continue
            
        if not (int(number) % int(digit)):
            count += 1

    print count    