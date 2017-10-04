class node:
    
    def __init__(self, val):
        
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        root = node(val)
    else:
        if root.val>val:
            if root.left == None:
                root.left = node(val)
            else:
                insert(root.left, val)
        else:
            if root.right == None:
                root.right = node(val)
            else:
                insert(root.right, val)

def inorder(root):
    if root:
        inorder(root.left)
        print root.val,
        inorder(root.right)
        

def inorder_pre(root, val):
    pre = None
    while root:
        if root.val<val:
            pre = root
            root = root.right
        else:
            root = root.left
    return pre.val


def inorder_succ(root, val):
    suc = None
    while root:
        if root.val>val:
            suc = root
            
            root = root.left
        else:
            root = root.right
    return suc.val
        
root = node(50)
insert(root, 30)
insert(root, 60)
insert(root, 40)
insert(root, 10)
insert(root, 90)

inorder(root)
print "\nInorder successor of %d is %d" %(40 ,inorder_pre(root,40))
print "\nInorder predecessor of %d is %d" %(40, inorder_succ(root,40))

            
    
