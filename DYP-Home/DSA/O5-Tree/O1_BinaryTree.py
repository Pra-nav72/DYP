class Node:
    def __init__(self, Value):
        self.left = None
        self.data = Value
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertL(self, data):
        data = Node(data)

        if self.root is None:
            self.root = data
        else:
            self.root.left = data