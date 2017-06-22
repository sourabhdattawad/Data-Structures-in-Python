array = [4,3,87,21,2,6,1]
for i in range(len(array)):
    for j in range(len(array)-1):
        if array[j]>array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print array


            
