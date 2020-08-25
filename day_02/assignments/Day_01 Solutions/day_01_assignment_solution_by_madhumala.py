# INPUT

text = input ('Enter the string: ')

# Process
# Output

import math
words = text.split()
print (words)
S = ''.join(words)
for ch in S:
    print(ch + ' ---> ' + str(S.count(ch)))
