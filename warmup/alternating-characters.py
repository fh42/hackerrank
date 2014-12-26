# topic:   hackerrank.com
# problem: alternating characters
# author:  frank havemann
# date:    2014-12-26

import sys

def consecutive_chars( characters ):
    deletions = 0
    for i in range(0,len(characters)-1):
        if characters[i] == characters[i+1]:
            deletions += 1
    return deletions

cntTestCases = int(raw_input())

for i in range(0,int(cntTestCases)):
    record = raw_input()
    print consecutive_chars( record )