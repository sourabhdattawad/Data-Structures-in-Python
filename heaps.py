heap = [20,10,15,8,9,8]

def insert(ele):
    heap.append(ele)
    reorder(len(heap)-1)
    
def reorder(n):
    p = (n-1)/2
    if p>=0: 
        if(heap[p]<heap[n]):
            heap[p], heap[n] = heap[n], heap[p]
        reorder(p)
    return

def delete():
    heap[0] = heap.pop()
    reorder(len(heap)-1)

insert(21)
print heap

# insert(50)
# print heap

delete()
print heap
insert(50)
print heap
insert(50)
print heap
