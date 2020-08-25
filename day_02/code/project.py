# Project B

# Take a serveral numbers from the user
# Filter out the maximum, minmum, average, median, mode
# and prime numbers from the inputs

from primes import checkprime
from statistics import mode
import numpy as np

# inputs

L = []
while True:
    n = input("--> q to quit ")
    if(n.lower() == 'q'):
        break
    elif(n.isdigit()):
        L.append(int(n))
    else:
        continue

# Process and Output

primes = []
for n in L:
    if(checkprime(n)):
        primes.append(n)
        
print('-'*80)

print('MAXIMUM    :', max(L))
print('MINIMUM    :', min(L))
print('AVERAGE    :', sum(L)/len(L))
print('MEDIAN     :', np.median(L))
print('MODE       :', mode(L))
print('PRIMES     :', primes)


m = L[0]
for i in range(1, len(L)):
    if(L[i] > m):
        m = L[i]

print('C Style Maximum: ', m)

        

        


