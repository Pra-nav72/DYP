class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        
        new_node.next = self.rear
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Can't Dequeue, Empty List!")
            return
        temp = self.rear
        self.rear = temp.next
        del temp.value

    def display(self):
        if self.front is None:
            print("Can't display, Empty Queue!")
            return
        
        temp = self.rear
        
        while temp:
            print(" <-- ", temp.value, end="")
            temp = temp.next


q = Queue()
q.enqueue(23)
q.enqueue(23234)
q.enqueue(2)
q.enqueue(222)
q.enqueue(8882)
q.dequeue()
q.display()
