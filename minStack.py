# Design a stack that supports getMin() in O(1) time and O(1) extra space

class Stack:
    def __init__(self):
        self.array =[]
        self.min_val = 0
        
    def push(self, val):
        
        if self.array ==[]:
            self.min_val = val
        else:
            if val<self.min_val:
                self.min_val = val
        
        self.array.append([val,self.min_val])
    
    def pop(self):
        if self.array ==[]:
            return None
        k = self.array.pop()
        return k[0]
    
    def getMin(self):
        if self.array ==[]:
            return None
        k = self.array[-1]
        return k[1]

    
minStack = Stack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(2)
print minStack.getMin()
print minStack.pop()
print minStack.pop()
print minStack.getMin()





