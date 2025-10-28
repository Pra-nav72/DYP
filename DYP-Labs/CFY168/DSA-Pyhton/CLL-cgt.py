class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the circular linked list."""
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

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
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

    def insert_at_position(self, data, position):
        """Insert a new node at a given position (1-based index)."""
        if position < 1:
            print("Position should be >= 1")
            return

        new_node = Node(data)

        if position == 1:
            self.insert_at_beginning(data)
            return

        temp = self.head
        index = 1
        while index < position - 1 and temp.next != self.head:
            temp = temp.next
            index += 1

        # Insert node
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Delete the first occurrence of a node by value."""
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        prev = None

        # Case 1: Deleting head node
        if current.data == key:
            # If there's only one node
            if current.next == self.head:
                self.head = None
                return
            # Move to last node to update its next pointer
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            return

        # Case 2: Deleting non-head node
        prev = current
        current = current.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"Value {key} not found in list.")

    def search(self, key):
        """Search for a node and return True if found, else False."""
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        """Display all elements of the circular linked list."""
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        print("Circular Linked List elements:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()

    # Insert elements
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_beginning(5)
    cll.insert_at_position(15, 3)

    cll.display()

    # Search
    print("Search 20:", cll.search(20))
    print("Search 99:", cll.search(99))

    # Delete nodes
    cll.delete_node(5)
    cll.delete_node(2000)

    cll.display()
