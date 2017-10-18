x = bin(x)
y = bin(y)

xbin = x.split('b')[1]
ybin = y.split('b')[1]

x_len = len(xbin)
y_len = len(ybin)

dif = abs(x_len-y_len)
if x_len>y_len:
    ybin = "0"*dif+ybin
else:
    if y_len>x_len:
        xbin="0"*dif+xbin
count = 0
for i in range(len(xbin)):
    if xbin[i]!=ybin[i]:
        count+=1
return count
