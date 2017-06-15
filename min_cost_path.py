cost_matrix = [[3,2,8],[1,9,7],[0,5,2],[6,4,3]]
#Using Recursion 
def re_min_cost(m,n):
    if m<0 or n<0:
        return 9999
    if m==0 and n==0:
        return cost_matrix[m][n]
    return cost_matrix[m][n]+min(re_min_cost(m-1,n-1),re_min_cost(m-1,n), re_min_cost(m,n-1))
print re_min_cost(3,2)

#Using Dynamic Programming
def dp_min_cost(m,n):
    for i in range(1, len(cost_matrix)):
        cost_matrix[i][0]= cost_matrix[i][0]+cost_matrix[i-1][0]
    
    for i in range(1, len(cost_matrix[0])):
        cost_matrix[0][i]= cost_matrix[0][i]+cost_matrix[0][i]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost_matrix[i][j] = cost_matrix[i][j]+min(cost_matrix[i-1][j],cost_matrix[i-1][j-1],cost_matrix[i][j-1])
    return cost_matrix[m][n]
print dp_min_cost(3,2)
        
