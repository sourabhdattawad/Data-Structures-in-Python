steps = [2,3,1,1,2,4,2,0,1,1]
arr = [9999 for i in range(len(steps))]
arr[0] = 0
for i in range(len(steps)-1):
    for j in range(1, steps[i]+1):        
        arr[i+j] = min(arr[i]+1, arr[j+i])
print arr[-1]
        
