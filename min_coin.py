coins =[1, 2, 5, 10, 20, 50, 100, 500, 1000]
coins.sort(reverse = True)
sum1 = 43
count = 0
i = 0
while (sum1!=0):
    if coins[i]<=sum1:
        sum1-=coins[i]
        count+=1
        print coins[i],
    else:
        i+=1
