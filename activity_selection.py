a = [1,3,0,5,8,5]
b = [2,4,6,7,9,9]
c =[]
for i in range(len(a)):
    c.append((a[i],b[i]))
def cusort(a,b):
    return a[1]-b[1]
c.sort(cmp = cusort)
print 0,
prev = c[0][1]
for i in range(1,len(c)):
    start = c[i][0]
    if start>prev:
        print i,
        prev = c[i][1]
        
    
    
    
