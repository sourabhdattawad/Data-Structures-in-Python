a = [1,2,100]

profit = 0 
maxi = 0
for i in range(len(a)-1,-1,-1):
    current = a[i]
    if current>=maxi:
        maxi = current
    profit+=(maxi-current)
print profit



#Kadane's algorithm

a =[7, 1, 5, 3, 6, 4]

max_curr = 0
max_pro = 0
for i in range(1, len(a)):
    max_curr += a[i]-a[i-1]
    if max_curr<0:
        max_curr = 0
    else:
        if max_curr>max_pro:
            max_pro = max_curr
print max_pro
    
    

        
