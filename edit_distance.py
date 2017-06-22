string1 = "sunday"
string2 = "saturday"

matrix = []
for i in range(len(string1)+1):
    matrix.append([0 for i in range(len(string2)+1)])
for i in range(len(matrix)):
    matrix[i][0] = i
for i in range(len(matrix[0])):
    matrix[0][i] = i
for i in range(1,len(matrix)):
    for j in range(1, len(matrix[0])):
        if string1[i-1]== string2[j-1]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = 1+min(matrix[i-1][j-1],matrix[i][j-1],matrix[i-1][j])
print "Min edit distance is",matrix[-1][-1]
    
    
