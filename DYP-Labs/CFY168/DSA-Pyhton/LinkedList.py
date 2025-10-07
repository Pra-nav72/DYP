class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def insert(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LinkedList is not empty")

l =[12, 34, 67, 222, "hello"]
for i in l:
    linkedList.insert(i)


