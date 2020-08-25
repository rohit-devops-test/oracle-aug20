# Guess my number game

import random

# choose a random number between 1 and 100

cn = random.randint(1, 100)

# instructions to the user

print('------------------------------------------------------')
print('       WELCOME TO THE GUESS MY NUMBER GAME            ')
print('The computer has chosen a number between 1 and 100 and')
print('you need to guess it. Maximum trials is 10            ')
print('------------------------------------------------------')

trials = 1
while True:

    if(trials > 10):
        break
    
    # ask the user guess

    un = int(input('Your guess --> '))

    # compare the chosen number and the user number
    # if they are same, then game over
    # else, give hints to the user to make the next guess and update the trials
    # repeat the process
    # but if trials > 10, game over

    if(un == cn):
        print('Congratulations!')
        break
    elif(un > cn):
        print('Guess a smaller number')
        trials += 1
    else:
        print('Guess a higher number')
        trials += 1
    

# game over -> print results

print('-'*60)

if(trials <= 3):
    print('Excellent playing!')
elif(3 < trials < 8):
    print('You\'re good')
else:
    print('Needs improvement')
    
