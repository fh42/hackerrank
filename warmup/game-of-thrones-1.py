# topic:   hackerrank.com
# problem: Game of Thrones - 1
# author:  frank havemann
# date:    2014-12-28


string = raw_input()
 
found = False

# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

# initialize variables
_LETTERS_ = 26
count = [0] * (_LETTERS_ + 1) # one for counting odds


# count every single character within input
for c in string:
	count[ord(c) - ord('a')] += 1

for n in range(0,_LETTERS_):
	if count[n] % 2 != 0:
		count[_LETTERS_] += 1

# determine if the input as even or odd characters
max_odd_chars = 0 if len(string) % 2 == 0 else 1

# determine if palindrome permutation is possible
found = True if count[_LETTERS_] == max_odd_chars else False

if not found:
    print("NO")
else:
    print("YES")