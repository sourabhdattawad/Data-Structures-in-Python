def GCD(A,B):
    while(B!=0):
        rem  = A%B
        GCD(B,rem)
        A = B
        B = rem
    return A
A = 5
B = 3
LCM = (A/GCD(A,B))*B
print LCM
    
