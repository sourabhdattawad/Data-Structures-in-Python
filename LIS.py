#Dynamic programming

array = [12, 18, 7, 34, 30, 28, 90, 88]
max_len_array = [0 for i in range(len(array))]
max_len_array[0] = 1
for  i in range(1, len(array)):
    max_len_array[i] = 1
    for j in range(0, i):
        if array[j]<array[i] and max_len_array[i]< max_len_array[j]+1:
            max_len_array[i] = max_len_array[j]+1
print max_len_array[-1]
