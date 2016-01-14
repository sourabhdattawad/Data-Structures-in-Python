def GCD(A,B):
    while(B!=0):
        rem  = A%B
        GCD(B,rem)
        A = B
        B = rem
    return A
GCD(7809999998,6300009)
    
