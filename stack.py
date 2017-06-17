class Queue:
    def __init__(self):
        self.array =[]
        
    def add(self, val):
        self.array.append(val)
        
    def remove(self):
        return self.array.pop()
    
    def print_queue(self):
        return self.array

myQueue = Queue()
myQueue.add(1)
myQueue.add(2)
myQueue.add(3)
myQueue.add(4)
print myQueue.print_queue()
print myQueue.remove()
print myQueue.remove()
print myQueue.print_queue()
