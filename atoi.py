a = '1234'
n = 1
res = 0
for i in range(len(a)-1,-1,-1):
    k = ord(a[i])%48
    res+=(k*n)
    n*=10
print res
    
    
