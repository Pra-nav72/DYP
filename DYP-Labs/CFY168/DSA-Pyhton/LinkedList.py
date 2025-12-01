class Node:
    def __init__(self, data, prev):
        self.data = data
        self.prev = prev
        self.next = None  

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.prev = new_node 
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        
        temp.next = new_node


    def display(self):
        current = self.head
        if current is None:
            print("The linked list is empty.")
            return

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")

    def is_empty(self):
        return self.head is None
    

ll = DoublyLinkedList()
ll.insert(55)
ll.display()
