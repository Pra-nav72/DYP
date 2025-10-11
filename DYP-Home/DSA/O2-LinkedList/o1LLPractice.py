#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    #insert at the beginning of the list
    def add_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # insert at the end of the list
    def add_at_end(self, data):
        new_node = Node(data)

        # if list is empty 
        if self.head is None:
            self.head = new_node
            return
        # traverse to the last node
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    #insert in-between (after)
    def add_after(self, value, x):
        new_node = Node(x)

        #if list is empty
        if self.head is None:
            print("List is empty")
            return
        
        #traverse to find the value
        current = self.head
        while current and current.data != value:
            current = current.next

        if current is None:
            print(f"{x} is not in list!")
            return
            
        new_node.next = current.next
        current.next = new_node


    # insert in-between (before)
    def add_before(self, value, x):
        new_node = Node(x)

        if self.head is None:
            print("list head is empty!")
            return
        
        # value is in first node
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return
        
        #traverse to find the value
        prev = None
        current = self.head
        while current and current.data != value:
            prev = self.head
            current = current.next

        if current is None:
            print(f"{x}bef is not is List!")
            return
        
        prev.next = new_node
        new_node.next = current

    #deleting a Node
    def delete_data(self, value):

        current = self.head
        #if data is in head node
        if current and current.data == value:
            self.head = current.next
            current = None
            return

        # traverse to find the key/data to delete
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print(f"{value} is not in List!")
            return
        
        prev.next = current.next
        current = None
    
    #display the linked List
    def display(self):
        current = self.head

        #list is empty
        if current is None:
            print("List is empty!")
            return
        
        elements=[]
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print ( " --> ".join(elements), " --> ^^NONE^^")



ll = LinkedList()


ll.add_at_begin(1)
ll.add_at_end(3)
ll.add_after(1, "hello")
ll.add_before(3, 2)
ll.display()
ll.delete_data(3)
ll.display()

            


            