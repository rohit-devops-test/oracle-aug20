string = input("Please enter String : ")
list1=[]
for ch in string:
    if ch not in list1:
        list1.append(ch)
        print(str(ch) + '-->' + str(string.count(ch)))
