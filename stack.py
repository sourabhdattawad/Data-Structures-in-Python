class Stack:
    def __init__(self):
        self.array =[]
        
    def add(self, val):
        self.array.append(val)
        
    def remove(self):
        return self.array.pop()
    
    def print_stack(self):
        return self.array

myStack = Stack()
myStack.add(1)
myStack.add(2)
myStack.add(3)
myStack.add(4)
print myStack.print_stack()
print myStack.remove()
print myStack.remove()
print myStack.print_stack()
