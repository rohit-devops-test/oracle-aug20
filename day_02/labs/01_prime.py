# Program to determine if the number is prime

# Input

n = int(input('Enter a number: '))

# Process

prime = True

for i in range(2, n):
    if(n % i == 0):
        prime = False
        break

# Output

if(prime):
    print('The number is Prime')
else:
    print('The number is not prime')
