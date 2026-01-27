# Queue using singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear  = None

 # adding element from end
    def enqueue(self, data):
        data = Node(data)
        if self.rear is None:
            self.front = data
            self.rear = data
        else:
            self.rear.next = data
            self.rear = data
    # removing element from front
    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is Empty!")
        self.front = self.front.next
        if self.front is None:
            self.rear = None

    def isempty(self):
        return self.front is None
    
    def peek(self):
        if self.front is None:
            raise Exception("Queue is Empty!")
        return self.front.data
        
    def display(self):
        if self.front is None:
            print("Queue is Empty!")
        else:
            current = self.front
            while current != None:
                print(current.data)
                current = current.next


k = Queue()

k.enqueue(34)
k.enqueue(44)
k.enqueue(54)
k.enqueue("last added item")

k.display()

k.dequeue()
print("after dequeue!")
k.display()

print(f"is_empty: {k.isempty()}")
print(f"peek: {k.peek()}")