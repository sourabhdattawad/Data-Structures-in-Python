from math import sqrt
n = 50
primes=[i for i in range(n+1)]
primes[0] = 0
primes[1] = 0

for i in range(2, int(sqrt(n))+1):
    
    if(primes[i]!=0):
        
        for k in range(2,n+1):
            while(i*k<=n):
                primes[i*k]=0
                k+=1
           
newprimes=[]
for i in primes:
    if(i!=0):
        newprimes.append(i)
print newprimes
        


