intervals = [[1,3],[2,4],[5,7],[6,8]]

def custom(a,b):
    return a[0]-b[0]
    
intervals.sort(cmp =custom)
stack = []
for interval in intervals:
    if stack==[]:
        stack.append(interval)
    else:
        old = stack.pop()        
        if interval[0]<=old[1]:
            if interval[1]>old[1]:
                stack.append([old[0], interval[1]])
            else:
                stack.append(old)
                
        else:
            stack.append(old)
            stack.append(interval)
print stack
    
    
    
    
