#input


print(text1)

print(text1)


#process and #output

for ch in text1:
    if(prev == ch):
        # prev=ch
        continue
    c = text1.count(ch)
    prev=ch
    print(ch + "--->" , c)