class Queue_array:
    def __init__(self):
        self.queues = []
        self.front = None
        self.end = None
    
    def enque(self, value):
        self.queues.append(value)

    def deque(self):
        if self.is_empty():
            print("\nEmpty Queue!")
            return
        self.queues.pop(0)
    
    def is_empty(self):
        return len(self.queues) == 0

    def display(self):
        print("\n\nDisplaying: ")
        for i in self.queues:
            
            print(f" --> {i}", end=" ")

    def peek(self):
        if self.is_empty():
            print('\nempty')
            return
        print(f"\n\n peek: {self.queues[0]}")

q = Queue_array()

print(q.is_empty())
q.deque()
q.enque(23)
q.peek()
q.enque(3)
q.enque(13)
q.enque(1233)
q.display()
q.deque()
print(q.is_empty())
q.peek()
q.display()