#input



#process


for char in inputString:
    if char not in tempStr:
        #output
        print(char, ', ', inputString.count(char))
        tempStr = tempStr + char