LC =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
str1=input("Enter string: ")
str1=str1.lower()
for char1 in LC:
    count1=str1.count(char1)
    if count1 != 0:
        print(char1 + '---->' + str(count1))
