a = [1,2,100]

profit = 0 
maxi = 0
for i in range(len(a)-1,-1,-1):
    current = a[i]
    if current>=maxi:
        maxi = current
    profit+=(maxi-current)
print profit
