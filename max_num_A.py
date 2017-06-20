#Let us assume that we have a specially made keyboard which has following four keys:  
#Key 1:  This key prints character 'A' on the output screen
#Key 2: (Ctrl-A): This keys selects the complete contents of the screen - same function as (Ctrl + A) of PC
#Key 3: (Ctrl-C): This key copies the seleceted content to buffer or clipboard - same function as (Ctrl + C) of PC  
#Key 4: (Ctrl-V): This key appends saved contents of buffer/clipboard to the output screen.  
#If you are allowed to press keys of this special keyboard N times, write a program which calculates maximum numbers of As possible.

n = 12
f  = [i for i in range(n+1)]
if n<7:
    print n
else:
    k = 7
    for i in range(k, n+1):
        max_val = i
        mul = 2
        for j in range(i-3,0,-1):
            k = mul*f[j]
            if k>max_val:
                max_val = k
                
            mul+=1
        f[i] = max_val
print f[-1]
        
            

        
