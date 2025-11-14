#reverse string using stack (lisked list implelmentation)
#Node class
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
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data
    
    def is_empty(self):
        return self.top is None
    
#function to reverse string using stack(linked list)
def reverse_string_using_stack(string):
    stack = Stack()
    s1 = []

    #push all charactes
    for ch in string:
        stack.push(ch)
        
    #pop all characters and store in s1
    while not stack.is_empty():
        s1.append(stack.pop())
    return ''.join(s1)
    
s = "Pranav"
s1 = reverse_string_using_stack(s)
print(f"given string {s}")
print(f"rversed string: {s1}")