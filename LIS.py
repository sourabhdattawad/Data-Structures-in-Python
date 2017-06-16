#Dynamic programming

array = [12, 18, 7, 34, 30, 28, 90, 88]
max_len_array = [1 for i in range(len(array))]
for  i in range(0, len(array)):
    for j in range(0, i):
        if array[j]<array[i] and max_len_array[i]< max_len_array[j]+1:
            max_len_array[i] = max_len_array[j]+1
print max(max_len_array[-1])
