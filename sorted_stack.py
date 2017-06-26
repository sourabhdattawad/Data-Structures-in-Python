class stack:
    
    def __init__(self):
        self.array = []
        
    def push(self,val):
        
        if self.array==[]:
            self.array.append(val)
        else:
            temp = []
            if val<self.array[-1]:
                while(self.array[-1]>val):
                    temp.append(self.array.pop())
                    if self.array ==[]:
                        break
                self.array.append(val)
                while temp:
                    self.array.append(temp.pop())
                
            else:
                self.array.append(val)
                
                            
    def pop(self):
        return self.array.pop()
    
    def display(self):
        return self.array
    

mystack = stack()
mystack.push(1)
mystack.push(3)
mystack.push(2)
mystack.push(4)
mystack.push(0)
mystack.pop()



                    
