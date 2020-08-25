#input

text1 = input("Please enter the text")
print(text1)
text1=sorted(text1)
print(text1)


#process and #output
prev=""
for ch in text1:
    if(prev == ch):
        # prev=ch
        continue
    c = text1.count(ch)
    prev=ch
    print(ch + "--->" , c)
