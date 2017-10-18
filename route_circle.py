string = "LURD"
x = 0
y = 0

for i in range(len(string)):
    if string[i]=="U":
        y = y+1
    elif string[i]=="D":
        y = y-1
    elif string[i]=="L":
        x = x-1
    else:
        x = x+1

if x==0 and y==0:
    return True
else:
    return False
        
        
