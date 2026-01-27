# Dequeue ==> Double Ended Queue (using singly linked list)
# i.e. insertion and deletion from both end

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insertFront(self, data):
        data = Node(data)
        if self.front is None:
            self.front = data
            self.rear = data
        else:
            data.next = self.front
            self.front = data

    def insertRear(self, data):
        data = Node(data)
        if self.front is None:
            self.front = data
            self.rear = data
        else:
            self.rear.next = data
            self.rear = data

    def deleteFront(self):
        if self.front is None:
            raise Exception("Queue is empty!")
        self.front = self.front.next

    def deleteRear(self):
        if self.rear is None:
            raise Exception("Queue is empty!")
        
        if self.front.next is None:
            self.front = None
            self.rear = None
            return
        
        current = self.front
        while current.next != self.rear:
            current = current.next

        current.next= None
        self.rear = current

    def display(self):
        if self.front is None:
            print("Empty Queue!")
        else:
            current = self.front
            while current != None:
                print(current.data)
                current = current.next

d = Dequeue()

d.insertFront(45)
d.insertFront(35)
d.insertRear(55)
d.insertRear(65)

d.display()

d.deleteFront()
d.deleteRear()

print("after deleting front & rear")

d.display()