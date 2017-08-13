# Given an array A[] and a number x, check for pair in A[] with sum as x

a = [-8,1,4,6,10,45]
a.sort()
l = 0
r = len(a)-1
found = 0
target = 16
while(not found):
    if l>r or r<l:
        break
    else:
        temp = a[l]+a[r]
        if temp==target:
            found=1
        elif temp>target:
            r-=1
        else:
            l+=1
print found
            
        
    
