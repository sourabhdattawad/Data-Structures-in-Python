a = "geeksforgeeks"
b = "for"
found = False
blen  = len(b)
for i in range(len(a)):
    if a[i] == b[0]:
        if a[i:i+blen]==b:
            found = True
            print i
            break
if not found:
    print -1
            
