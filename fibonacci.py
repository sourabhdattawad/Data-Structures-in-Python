n = 8

#Using Recursion
def fib_recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)
print fib_recursion(8)




#Using DP
fib = [0 for i in range(n+1)]
fib[0] = 0
fib[1] = 1
for i in range(2, n+1):
    fib[i] = fib[i-1]+fib[i-2]
print fib[-1]
