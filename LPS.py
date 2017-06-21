string = "abbabb"
matrix = [[False for i in range(len(string))] for i in range(len(string)) ]

for i in range(len(matrix)):
    matrix[i][i] = True

max_val = 0
start = 0
for L in range(2, len(string)+1):    
    for i in range(0, len(string)-L+1):
        if L==2:
            if string[i] == string[i+1]:
                matrix[i][i+1] = True
                max_val = L
                start = i
        else:
            j = i+L-1
            if (string[i]==string[j]):
                if L>max_val:
                    max_val = L
                    start  = i
                
            matrix[i][j] = (string[i]==string[j]) and matrix[i+1][j-1]
            
            
print max_val
print string[start:start+L]
