class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


        

class ll:
    
    def __init__(self):
        self.head = None
        
    def insert(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
    
    def print_nodes(self):
        curr = self.head
        
        while(curr!=None):
            print curr.val,
            curr = curr.next
    def delete_key(self, key):
        curr = self.head
        prev = None
        while(curr!=None):
            if(curr.val==key):
                prev.next = curr.next
            prev = curr
            curr = curr.next
    
    def rec_len(self):
        return recursion_len(self.head)
    
    def mid_node(self):
        slow = self.head
        fast = self.head
        while(fast!=None and fast.next!=None):
            fast = fast.next
            fast = fast.next
            slow=slow.next
        print slow.val
        
    def get_head (self):
        return self.head
            
        
def recursion_len(curr):
    if curr==None:
        return 0
    else :
        return 1 + recursion_len(curr.next)
    
def merge():
    l3 = ll()
    l1 = link1.get_head()
    l2 = link2.get_head()
    while(l1!=None and l2!=None):
        if l1.val>l2.val:
            l3.insert(l2.val)
            l2 = l2.next
        else:
            l3.insert(l1.val)
            l1 = l1.next
    if l1==None:
        while(l2!=None):
            l3.insert(l2.val)
            l2 = l2.next
    if l2==None:
        while(l1!=None):
            l3.insert(l1.val)
            l1 = l1.next
    l3.print_nodes()
        

            

link1 = ll()
link1.insert(6)
link1.insert(5)
link1.insert(4)
# link1.insert(3)
# link1.insert(1)


link2 = ll()
link2.insert(7)
link2.insert(2)
link2.insert(1)
# link2.insert(6)
# link2.insert(5)

# link.delete_key(4)             
link1.print_nodes()
link1.rec_len()
print "\n"
link1.mid_node()
print "\n"
merge()
