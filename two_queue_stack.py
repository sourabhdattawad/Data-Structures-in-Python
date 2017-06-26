class stack:
    def __init__(self):
        
        self.q1= []
        self.q2 = []
    
    def push(self,val):
        
        self.q1.append(val)
        print self.q1
    
    def pop(self):
        if self.q1==[]:
            return None
        
        self.q2[:] = self.q1[0:len(self.q1)-1]
        k = self.q1.pop()
        self.q1[:] = self.q2[:]
        self.q2[:] = []
        
        return k
    def display(self):
        return self.q1

mystack = stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.pop()
mystack.display()
mystack.pop()
mystack.pop()
mystack.pop()
mystack.pop()
mystack.display()

        
        
        
        
        
        
        
        
