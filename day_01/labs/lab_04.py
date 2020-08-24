# Program to filter the 2 digit numbers whose sum of individual
# digits is some value say 10

# [100 random numbers]
# [filtered values]

# 64 => 6 + 4 = 10
# 33 => X
# 73 => & + 3 = 10

import random

# Input

RN = []
for i in range(100):
    RN.append(random.randint(10, 99))
print(RN)
print('_'*60)

# Process

FN = []
for n in RN:
    if((n//10 + n%10) == 10): # Manjeeth
        FN.append(n)


# Output

print(FN)


    

