array = [1,3,9,2]
array.sort()
sub_sum = 6
matrix = []
for i in range(len(array)+1):
    matrix.append([False for i in range(sub_sum+1)])
for i in range(len(matrix)):
    matrix[i][0]= True
for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        matrix[i][j] = matrix[i-1][j] or matrix[i-1][j-array[i-1]]
print matrix[-1][-1]
