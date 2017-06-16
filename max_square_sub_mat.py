#Dynamic programming

matrix = [[1, 1, 0, 0, 1, 1],[0, 0, 1, 0, 1, 1],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1],[1, 0, 0, 0, 1, 1]]
table = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix)) ]
max_sub_sq = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i==0 or j==0:
            table[i][j] = matrix[i][j]
            
        elif matrix[i][j]==0:
            table[i][j] = 0
        else:
            table[i][j] = min(table[i-1][j-1],table[i-1][j],table[i][j-1])+1
            if table[i][j]>max_sub_sq:
                max_sub_sq = table[i][j]
                
            
print max_sub_sq
