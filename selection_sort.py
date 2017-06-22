array = [4,3,87,21,2,6,1]
for i in range(len(array)):
    min_ele = array[i]
    index = i
    for j in range(i+1,len(array)):
        if array[j]<min_ele:            
            min_ele = array[j]
            index  = j
            
    temp = array[i]
    array[i] = array[index]
    array[index] = temp
    
print array

            
