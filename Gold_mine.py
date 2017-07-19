gold_mines = [[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]
max_sum = 0
current_sum = 0
max_array = []
for i in range(len(gold_mines)):
    current_sum = gold_mines[i][0]
    curr_array = [(i,0)]
    k = i
    j = 0

    while(j!=len(gold_mines[0])-1):
        
        if k==0:
            if gold_mines[k][j+1]<gold_mines[k+1][j+1]:
                k=k+1
            
        elif k==len(gold_mines)-1:
            if gold_mines[k][j+1]<gold_mines[k-1][j+1]:
                k=k-1
        
        else:
            
            if gold_mines[k][j+1]>gold_mines[k-1][j+1]>gold_mines[k+1][j+1]:
                k=k
            elif gold_mines[k-1][j+1]>gold_mines[k][j+1]>gold_mines[k+1][j+1]:
                k=k-1
            elif gold_mines[k+1][j+1]>gold_mines[k-1][j+1]>gold_mines[k][j+1]:
                k=k+1
                
        j+=1
        current_sum+=gold_mines[k][j]
        curr_array.append((k,j))
        
        if current_sum>max_sum:
            max_sum = current_sum
            max_array = curr_array
print max_sum
print max_array        
                
            
        
            
            
            
            
        
        
        
        
    
