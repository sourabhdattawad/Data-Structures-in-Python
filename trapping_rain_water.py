array = [0,1,0,2,1,0,1,3,2,1,2,1]
max_left = [ 0 for i in range(len(array))]
max_right = [ 0 for i in range(len(array))]
maxi = -1
for i in range(len(array)):
    if i==0:
        max_left[i] = -1
        maxi = array[i]
    else:
        max_left[i]= maxi
        if array[i]>maxi:
            maxi = array[i]
maxi = -1

for i in range(len(array)-1,-1,-1):
    if i==-1:
        max_right[i] = -1
        maxi = array[i]
    else:
        max_right[i]= maxi
        if array[i]>maxi:
            maxi = array[i]


res = 0
for i in range(1,len(array)-1):
    k = min(max_left[i],max_right[i])-array[i]
    if k>0:
        res+=k
print res
        
        
        
    
