string = input("Enter the string: ")
list = []
for s in string:
    count = 0
    if (s not in list) :
        if(s != " "):
            list.append(s)
            count = string.count(s) 
            print(s,' ---> ',count)
