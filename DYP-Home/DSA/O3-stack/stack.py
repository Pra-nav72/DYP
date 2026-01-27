class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    # adding value at the beginning
    def push(self, value):
        data = Node(value)
        data.next = self.top
        self.top = data
    
    # removing values from the beginning
    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty!")
        else:
            self.top = self.top.next

    # return last added value
    def peek(self):
        if self.top is None:
            raise Exception("stack is empty!")
        return self.top.value
    
    def isempty(self):
        return self.top is None
    
    def display(self):
        if self.isempty():
            print("stack is empty!")
        else:
            current = self.top
            while current != None:
                print(current.value)
                current = current.next


st = Stack()
st.push(32)
st.push(2)
st.push(46)
st.push(302)
st.push(2342)

st.display()

st.pop()
st.display()
y = st.peek()
print(y)