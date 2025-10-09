class Node:
    """
    An individual element in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node(next is just a variable), initialized to None

class LinkedList:
    """
    Manages the linked list and provides methods for list operations.
    """
    def __init__(self):
        # The 'head' is the starting point of the list
        self.head = None

    # ---------------------------------
    # 2.1. Insertion Methods
    # ---------------------------------

    def insert_at_beginning(self, data):
        """Inserts a new node at the start of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node 
            return

        # Traverse to the last node
        last = self.head
        while last.next:
            last = last.next
        
        # Link the last node's 'next' to the new node
        last.next = new_node

    # ---------------------------------
    # 2.2. insert Before
    # ---------------------------------

    def insert_before(self, value, x):
        new_node = Node(x)

        #case 1: list is empty
        if self.head is None:
            print("List is empty!")
            return
        
        #Case 2: value is in first node
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return
        
        #case 3: traverse to find the value
        current = self.head
        prev = None
        
        while current and current.data != value:
            prev = current
            current = current.next
        
        if current is None:
            print(f"{value} not found!")
            return
        new_node.next = current
        prev.next = new_node

    # ---------------------------------
    # 2.3. insert after
    # ---------------------------------
    def insert_after(self, value, x):
        new_node = Node(x)

    #     #case 1: List is empty
        if self.head is None:
            print("List is empty!")
            return
        
    #     #case 2: if value is at end
        current = self.head
        while current and current.data != value:
            current = current.next
            
        
        if current is None:
            print(f"{value} not found!")
            return

        new_node.next = current.next
        current.next = new_node

    # ---------------------------------
    # 2.4. Deletion Method
    # ---------------------------------

    def delete_node(self, key):
        """Deletes the first node that contains the matching 'key' data."""
        current = self.head

        # Case 1: Head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None # Delete the node
            return

        # Case 2: Search for the key to be deleted (keep track of the previous node)
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the list
        if current is None:
            print(f"Key '{key}' not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None # Delete the node

    # ---------------------------------
    # 2.3. Display Method
    # ---------------------------------

    def display(self):
        """Prints the data of all nodes in the list."""
        current = self.head
        if current is None:
            print("The linked list is empty.")
            return

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        # Print the list in the format: data -> data -> ... -> None
        print(" -> ".join(elements) + " -> None")

    # ---------------------------------
    # 2.4. Other Useful Method
    # ---------------------------------
    
    def is_empty(self):
        """Checks if the list is empty."""
        return self.head is None
    

ll = LinkedList()
ll.insert_at_beginning(55)
ll.insert_at_beginning(99)
ll.insert_at_end("end")
ll.insert_at_beginning(0)
ll.insert_at_beginning(None)
ll.insert_at_end(None)
ll.insert_at_end(55)
ll.insert_before("end", "inserting")
ll.insert_before(55, "inserting Again")
ll.display()
ll.delete_node(55)
ll.insert_after(None, 505)
ll.insert_after(55, " 55 again")
ll.display()

