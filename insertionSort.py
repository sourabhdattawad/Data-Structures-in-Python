# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Insertion Sort

a = [34, 12, 99, 56, 1, 8, 100,3]
for i in range(1, len(a)):
    temp = a[i]
    j = i-1
    while(j>=0 and temp<a[j]):
        a[j+1] = a[j]
        j-=1
    a[j+1] = temp
print a

# <codecell>


