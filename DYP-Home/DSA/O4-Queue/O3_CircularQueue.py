class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CicularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None
    
    def enqueue(self, value):
        data = Node(value)

        if self.isempty():
            self.front = data
            self.rear = data
            self.rear.next = self.front
        else:
            self.rear.next = data
            self.rear = data
            self.rear.next = self.front

    def dequeue(self):
        if self.isempty():
            raise Exception("Queue is empty!")
        
        if  self.front == self.rear:
            element = self.front.data
            self.front = None
            self.rear = None
            return element
        
        element = self.front.data
        self.front = self.front.next
        self.rear.next = self.front
        return element 
    
    def peek(self):
        if self.isempty():
            raise Exception("Circular Queue is Empty")
        return self.front.data

    def display(self):
        if self.isempty():
            print("Circular Queue is Empty")
            return

        current = self.front
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.front:
                break
        print()

c = CicularQueue()
c.enqueue(34)
c.enqueue(45)
c.enqueue(55)
c.enqueue(65)

c.display()

c.dequeue()
c.dequeue()

print("after dequeue:")
c.display()