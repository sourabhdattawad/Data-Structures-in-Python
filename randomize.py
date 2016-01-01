from random import randint
array=[1,2,76,31,54]
temp=0
print array
for i in range(len(array)-1,-1,-1):
    rnd = randint(0,i)
    temp = array[i]
    array[i] = array[rnd]
    array[rnd] = temp
print array
    
