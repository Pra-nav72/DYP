class stack1:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
   

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        
        for i in reversed(self.stack):
            print(i, "\n", "^")
            # print("^")

st = stack1()

st.push(23)
st.push(253)
st.push(232)
st.push(3323)
st.display()

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return None

#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         return None

#     def is_empty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)
    
#     def display(self):
#         for item in reversed(self.stack):
#             print((item), end="\n ^ ")


# # Example usage
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print("Top item:", s.peek())
# print("Popped:", s.pop())
# print("Stack size:", s.size())
# s.push(3)
# s.push("slkjdfls")
# s.push(343)
# s.display()
