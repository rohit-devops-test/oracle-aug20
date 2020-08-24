# Program to accept two numbers and
# print the difference
# print if the outcome is positive, negative or zero


# input

n1 = int(input('Enter a number: '))
n2 = int(input('Enter the second number: '))

# process

diff = n1 - n2

# output

print('_'*40)
print('DIFFERENCE: ', abs(n1 - n2))

if(diff > 0):
    print("POSITIVE")
elif(diff < 0):
    print("NEGATIVE")
else:
    print("ZERO")
