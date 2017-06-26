class Node:
    countme = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if(data>self.data):
            if(self.right == None):
                self.right = Node(data)
            else:
                self.right.insert(data)
        elif(data<self.data):
            if(self.left ==None):
                self.left = Node(data)
            else:
                self.left.insert(data)
    
    def inorder(self):
        if(self.left!=None):
            self.left.inorder()
        print self.data
        if(self.right!=None):
            self.right.inorder()
            
    def min_number(self):
        
        current=self.left
        while current.left!=None:
            current = current.left
        print current.data
        
    def is_bst(self, prev):
        if(self.left!=None):
            self.left.is_bst(prev)
        if prev>self.data:
            print "No"
        prev = self.data
        if(self.right!=None):
            self.right.is_bst(prev)
        
    def lca(self, n1, n2):
        current = self
        
        if  current.data>n1 and current.data<n2 or  current.data<n1 and current.data>n2:
            print current.data
            return
        
        while current.data>n1 and current.data>n2:
            if current.left.data >n1 and current.left.data>n2:
                current = current.left
            else:
                return current.data
                
        while current.data<n1 and current.data<n2:
            if current.right.data <n1 and current.right.data<n2:
                current = current.right
            else:
                return current.data
                
    def kth_smallest(self, k):
        
        if self.left!=None:
            self.left.kth_smallest(k)
        
        Node.countme+=1
        if k==Node.countme:
            print self.data
        
        if self.right!=None:
            self.right.kth_smallest(k)
   
    def level_order(self):
        queue = []
        root = self
        queue.append(root)
        while(queue !=[]):
            k = queue.pop(0)
            print k.data,
            if k.left!=None:
                queue.append(k.left)
                
            if k.right!=None:
                queue.append(k.right)
                
    def leaf(self):
    
        if (self.left!=None):
            self.left.leaf()
        if self.left==None and self.right==None:
            print self.data,
        if (self.right!=None):
            self.right.leaf()
            
  
                
root = Node(4)
root.insert(3)
root.insert(1)
root.insert(10)
root.insert(11)

root.insert(2)

# root.inorder()
# print "Min number"

# root.min_number()
# root.is_bst(-999)
# print "LCA"

# root.lca(2,1)
count = 0
root.kth_smallest(3)
    
