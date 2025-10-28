class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLL:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
               temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            print("List is empty!")
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next


        temp.next = new_node
        new_node.next = self.head


    def add_at_position(self, data, pos):

        if pos<1:
            print("position should not be less than 1")
            return           

        new_node = Node(data)

        if pos == 1:
            self.add_begin(data)
            return
        
        temp = self.head
        index = 1
        while index < pos-1 and temp.next != self.head:
            temp = temp.next
            index += 1
        
        new_node.next = temp.next
        temp.next = new_node

    
    def delete(self, data):
        if self.head is None:
            print("list is empty!")
            return
        
        #to delete head nod
        current = self.head
        prev = None

        if current.data == data:
            if current.next == self.head:
                self.head = None
                return
            
            #change last node pointer
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return

        #to delete non head node
        prev = current
        current = current.next
        while current != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next


        print(f"{data} not found!")


    def display(self):
        """Prints the data of all nodes in the list."""
        current = self.head
        if current is None:
            print("The linked list is empty.")
            return

        elements = []
        temp = self.head
        while True:
            # print(temp.data)
            elements.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        
        # Print the list in the format: data -> data -> ... -> None
        print(" -> ".join(elements) + " -> " + str(self.head.data))








cll = CircularLL()
cll.add_begin(23)
cll.add_begin(1)
cll.add_end("end")
cll.add_end("last-end")
# cll.add_begin(0)
cll.add_at_position("aa", 3)
cll.display()
cll.delete(1)
cll.display()