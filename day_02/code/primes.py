def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# Program to determine if the number is prime

if __name__ == "__main__":
    
    # Input

    n = int(input('Enter a number: '))

    # Output

    if(checkprime(n)):
        print('The number is Prime')
    else:
        print('The number is not prime')
