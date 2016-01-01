a=5
b=3
m=7
x=[0]
i=0
val=0
while(i<m-1):
    val=(x[i]*a+b)%m
    x.append(val)
    i+=1
print x

