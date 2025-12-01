#stack using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "stack is empty!"
        
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
       if self.top is None:
           print("Stack is empty")
       x = self.top
       while x:
           print(x.data)
           x = x.next
    
    
s = Stack()
print(s.is_empty())

s.push(34)
s.push(12)
s.push(45)
s.push(4)

print(s.is_empty())

s.display()
print ('-------------------------------- ')
s.pop()
s.display()

