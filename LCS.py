string1 = 'CLCC'
string2 = 'CLCLLLLLLL'

table = []

for i in range(len(string1)):
    table.append([0 for j in range(len(string2))])
max_len= 0
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i]==string2[j]:
            if i==0 or j==0:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j-1]+1
            max_len = max(table[i][j], max_len)
                
print max_len
