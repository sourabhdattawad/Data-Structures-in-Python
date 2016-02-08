number = 361121212
factors=[]
while(number%2==0):
    factors.append(2)
    number=number/2

factor =3
stop_at = math.sqrt(number)
while(factor<=stop_at):
    
    while(number%factor==0):
        factors.append(factor)
        number=number/factor
        stop_at = math.sqrt(number)
        if(stop_at == number):
            break
    factor+=2
    
if(number>1):
    factors.append(number)
print factors

    


