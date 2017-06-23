class Node:
    def __init__(self, val):
        self.next = None
        self.data = val
        
class linked_list:
    
    def __init__(self):
        self.head = None
        
    def add_node(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        current = self.head
        while current!=None:
            print current.data,
            current = current.next
            
    def reverse_list(self):
        current = self.head
        prev  = None
        while(current!=None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp    
        self.head  = prev
        
    def nth_node(self, num):
        current = self.head
        length = 0
        while(current!=None):
            length+=1
            current = current.next
        count = length-num
        current = self.head
        while(count):
            current = current.next
            count-=1
        print current.data
            

list = linked_list()
list.add_node(2)
list.add_node(5)
list.add_node(4)
list.add_node(1)
list.add_node(3)

list.print_list()
print "\n"
list.reverse_list()
print "\n"
list.print_list()
print "\n"
list.nth_node(2)

