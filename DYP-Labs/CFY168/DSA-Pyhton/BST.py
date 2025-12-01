class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    # INSERT
    def insert(self, key, node=None):
        if self.root is None:
            self.root = Node(key)
            return self.root
        
        if node is None:
            node = self.root

        if key<node.data:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert(key, node.right)
        
        return self.root
    
    #find MINIMUM
    
    # Traversal
    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)
    
    def preOrder(self, node):
        if node:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.preOrder(node.right)
            print(node.data, end=" ")

b = BST()
b.insert(34)
b.insert(11)
b.insert(44)

b.insert(32)
print("\n------------inorder-----------\n")
b.inOrder(b.root)
print("\n------------pre-order-----------\n")
b.preOrder(b.root)
print("\n------------post-order-----------\n")
b.postOrder(b.root)