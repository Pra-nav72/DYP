class Node:
    """
    An individual element in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node, initialized to None

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
    # 2.2. Deletion Method
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
    


