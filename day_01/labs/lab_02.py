# input a string from the user
# determine if the string is a palidrome and output the result

# s = 'madam'
# This is a Palindrome

# s = 'may'
# This is not a Palindrome

# input

s = input('Enter a string: ' )

# process

# Rohit
# Shivanee
# Arun

if(s[::-1] == s):
    res = "This is a Palindrome"
else:
    res = "This is not a Palindrome"


# output

print(res)
