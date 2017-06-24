class Node:
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
    def preorder(self):
        print self.data
        if(self.left!=None):
            self.left.inorder()
        if(self.right!=None):
            self.right.inorder()
    def postorder(self):
        if(self.left!=None):
            self.left.inorder()
        if(self.right!=None):
            self.right.inorder()
        print self.data
    
    def no_sibling(self):
        if(self.left==None and self.right!=None):
            print self.right.data
        elif(self.left!=None and self.right==None):
            print self.left.data

        if(self.left!=None):
            self.left.no_sibling()
        if(self.right!=None):
            self.right.no_sibling()

    def search(self, data):
        if(data==self.data):
            print "Found"
            return
        else:
            if(data<self.data):
                if(self.left!=None):
                    self.left.search(data)
            elif(data>self.data):
                if(self.right!=None):
                    self.right.search(data)
    
    def leaf_nodes(self):
        if(self.left==None and self.right==None):
            print self.data
        if(self.left!=None):
            self.left.leaf_nodes()
        if(self.right!=None):
            self.right.leaf_nodes()
    
    def depth(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return self.right.depth() + 1
        elif self.right == None:
            return self.left.depth() + 1
        else:
            return max(self.left.depth(), self.right.depth()) + 1

        
        
        
        
                
root = Node(4)
root.insert(3)
root.insert(1)
root.insert(10)
root.insert(2)

# root.inorder()
# root.preorder()
root.no_sibling()
# root.search(3)
# root.leaf_nodes()
root.depth()          
            
            
    
    
